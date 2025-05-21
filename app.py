from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os
import logging
from logging.handlers import RotatingFileHandler

# Configure logging
def setup_logging(app):
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/car_evaluation.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Car Evaluation startup')

class Config:
    """Application configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-please-change-in-production'
    MODEL_PATH = os.path.join('save_models', 'model.pkl')
    SCALER_PATH = os.path.join('save_models', 'scaler.pkl')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size

class CarFeatureLabels:
    """Class to manage car feature label mappings"""
    
    BUYING_LABELS = {0: 'Low', 1: 'Medium', 2: 'High', 3: 'Very High'}
    MAINT_LABELS = {0: 'Low', 1: 'Medium', 2: 'High', 3: 'Very High'}
    DOORS_LABELS = {2: '2', 3: '3', 4: '4', 5: '5 or more'}
    PERSONS_LABELS = {2: '2', 4: '4', 6: 'More than 5'}
    LUGGAGE_LABELS = {0: 'Small', 1: 'Medium', 2: 'Big'}
    SAFETY_LABELS = {0: 'Low', 1: 'Medium', 2: 'High'}
    
    CLASS_LABELS = {
        0: 'unacceptable',
        1: 'acceptable',
        2: 'good',
        3: 'very good'
    }
    
    @classmethod
    def get_input_labels(cls, input_data):
        """Convert numeric input values to human-readable labels"""
        return {
            'buying': cls.BUYING_LABELS.get(int(input_data['buying']), 'Unknown'),
            'maintenance': cls.MAINT_LABELS.get(int(input_data['maintenance']), 'Unknown'),
            'doors': cls.DOORS_LABELS.get(int(input_data['doors']), 'Unknown'),
            'persons': cls.PERSONS_LABELS.get(int(input_data['persons']), 'Unknown'),
            'luggage': cls.LUGGAGE_LABELS.get(int(input_data['luggage']), 'Unknown'),
            'safety': cls.SAFETY_LABELS.get(int(input_data['safety']), 'Unknown')
        }


class CarEvaluationModel:
    """Class to handle the car evaluation prediction model"""
    
    def __init__(self, model_path='save_models/model.pkl'):
        """Initialize the model from the pickle file"""
        self.model = self._load_model(model_path)
    
    def _load_model(self, model_path):
        """Load the model from the pickle file"""
        try:
            return pickle.load(open(model_path, 'rb'))
        except Exception as e:
            print(f"Error loading model: {e}")
            return None
    
    def predict(self, features):
        """Make a prediction using the loaded model"""
        if self.model is None:
            raise ValueError("Model not loaded properly")
        
        # Convert features to numpy array if not already
        if not isinstance(features, np.ndarray):
            features = np.array(features)
            
        # Ensure features have the right shape
        if len(features.shape) == 1:
            features = features.reshape(1, -1)
            
        prediction = self.model.predict(features)
        return CarFeatureLabels.CLASS_LABELS.get(prediction[0], 'unknown')


class CarEvaluationApp:
    """Main application class for the Car Evaluation web app"""
    
    def __init__(self):
        """Initialize the Flask app and model"""
        self.app = Flask(__name__, static_folder='static')
        self.app.config.from_object(Config)
        
        # Set up logging
        setup_logging(self.app)
        
        # Initialize the model
        try:
            self.model = CarEvaluationModel()
            self.app.logger.info('Model loaded successfully')
        except Exception as e:
            self.app.logger.error(f'Error loading model: {str(e)}')
            raise
        
        # Set up error handlers
        self.setup_error_handlers()
        self._setup_routes()
    
    def setup_error_handlers(self):
        """Set up custom error handlers"""
        @self.app.errorhandler(404)
        def not_found_error(error):
            return render_template('error.html', error='Page not found'), 404

        @self.app.errorhandler(500)
        def internal_error(error):
            self.app.logger.error('Server Error: %s', str(error))
            return render_template('error.html', error='Internal server error'), 500

    def _setup_routes(self):
        """Set up the URL routes for the application"""
        self.app.add_url_rule('/', 'home', self.home, methods=['GET'])
        self.app.add_url_rule('/predict', 'predict', self.predict, methods=['POST'])

    def home(self):
        """Render the home page with the input form"""
        return render_template('input.html')

    def predict(self):
        """Process form data and make a prediction"""
        try:
            if request.method == 'POST':
                # Get form data
                form_data = request.form
                
                # Log prediction request
                self.app.logger.info(f'Prediction request received with data: {form_data}')
                
                # Extract features from form data
                features = [
                    int(form_data['buying']),
                    int(form_data['maintenance']),
                    int(form_data['doors']),
                    int(form_data['persons']),
                    int(form_data['luggage']),
                    int(form_data['safety'])
                ]
                
                # Make prediction
                prediction = self.model.predict(features)
                
                # Get human-readable labels for input values
                input_labels = CarFeatureLabels.get_input_labels(form_data)
                
                # Log successful prediction
                self.app.logger.info(f'Successful prediction: {prediction}')
                
                # Render results page
                return render_template(
                    'result.html',
                    prediction=prediction,
                    prediction_class=prediction,
                    input_labels=input_labels
                )
                
        except Exception as e:
            self.app.logger.error(f'Error during prediction: {str(e)}')
            return render_template('error.html', error=str(e))

    def run(self, debug=False, host='0.0.0.0', port=None):
        """Run the Flask application"""
        if port is None:
            port = int(os.environ.get('PORT', 5000))
        self.app.run(debug=debug, host=host, port=port)


# Create and run the application when this script is executed
if __name__ == '__main__':
    app = CarEvaluationApp()
    app.run(debug=True)

