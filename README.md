# Car Evaluation Application

This application predicts car acceptability based on various features using a machine learning model.

## Project Structure
```
app.py              # Main Flask application
car.ipynb           # Jupyter notebook for analysis
model.pkl           # Trained machine learning model
src/                # Source code directory
  data_loader.py    # Functions to load data
  eda.py            # Exploratory data analysis
  models.py         # Model definitions
  preprocess.py     # Data preprocessing functions
  test.py           # Unit tests
  train.py          # Model training script
static/css/         # CSS stylesheets
templates/          # HTML templates
```

## Setup Instructions

### Option 1: Using the Setup Script

The easiest way to set up the project is using the provided setup script:

```bash
# Make the script executable
chmod +x setup.sh

# Run the setup script
./setup.sh
```

This will create a virtual environment, install all required dependencies, and provide instructions for running the application.

### Option 2: Manual Setup

#### 1. Create a Virtual Environment

```bash
# For Python 3
python -m venv venv

# Activate the virtual environment
# On Linux/Mac
source venv/bin/activate
# On Windows
# venv\Scripts\activate
```

#### 2. Install Required Packages

```bash
# Install from requirements.txt
pip install -r requirements.txt
```

## Running the Application

```bash
# Start the Flask application
python app.py
```

The application will be available at http://localhost:5000

## Features
- Predicts car evaluation based on multiple parameters
- User-friendly web interface with separate input and result views
- Real-time predictions
- Object-oriented design for better code organization

## Input Parameters
- **Buying Price**: 0 (low) to 3 (very high)
- **Maintenance Price**: 0 (low) to 3 (very high)
- **Doors**: 2-5 (use 5 for '5more')
- **Persons**: 2-6 (use 6 for 'more')
- **Luggage Boot**: 0 (small), 1 (medium), 2 (big)
- **Safety**: 0 (low), 1 (medium), 2 (high)

## Development

For development with automatic reloading:

```bash
FLASK_APP=app.py FLASK_ENV=development flask run
```

For data analysis and model exploration:

```bash
jupyter notebook car.ipynb
```

## Deployment Guide

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Git
- Virtual environment tool (venv)

### Local Deployment

1. Clone the repository and navigate to the project directory:
```bash
git clone <repository-url>
cd car-evaluation-main
```

2. Create and activate a virtual environment:
```bash
# On Windows
python -m venv venv
.\venv\Scripts\Activate

# On Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set environment variables:
```bash
# On Windows PowerShell
$env:SECRET_KEY="your-secret-key-here"
$env:FLASK_ENV="production"

# On Linux/Mac
export SECRET_KEY="your-secret-key-here"
export FLASK_ENV="production"
```

### Production Deployment

#### Using Gunicorn (Linux/Unix)

1. Install Gunicorn (already in requirements.txt):
```bash
pip install gunicorn
```

2. Start the application:
```bash
gunicorn wsgi:application -c gunicorn.conf.py
```

#### Using Windows (Production)

For Windows production deployment, we recommend using Windows Subsystem for Linux (WSL) or a containerized solution with Docker.

#### Docker Deployment

1. Build the Docker image:
```bash
docker build -t car-evaluation-app .
```

2. Run the container:
```bash
docker run -d -p 8000:8000 car-evaluation-app
```

### Cloud Deployment (Render.com)

1. Create a free account on [Render.com](https://render.com)

2. Connect your GitHub repository:
   - Go to your Render dashboard
   - Click "New +" and select "Web Service"
   - Connect your GitHub repository
   
3. Configure the web service:
   - Name: car-evaluation (or your preferred name)
   - Environment: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn wsgi:application`
   
4. Set environment variables:
   - Click on "Environment" tab
   - Add the following variables:
     - `PYTHON_VERSION`: 3.9.0
     - `PORT`: 8000
     
5. Deploy:
   - Click "Create Web Service"
   - Wait for the deployment to complete

Your application will be available at: https://your-app-name.onrender.com

### Alternative Hosting Options

1. **Heroku**:
   - Similar setup to Render
   - Uses Procfile (already included)
   - Free tier discontinued, requires paid plan

2. **PythonAnywhere**:
   - Good for Python applications
   - Has a free tier
   - WSGI configuration required

3. **DigitalOcean App Platform**:
   - More control over infrastructure
   - Paid service
   - Good for scaling

Choose the platform based on your needs:
- Render.com: Easy deployment, free tier available
- PythonAnywhere: Python-focused, free tier available
- DigitalOcean: More control, paid service

### Security Considerations

1. Always set a strong SECRET_KEY in production
2. Enable HTTPS in production
3. Configure proper logging
4. Implement rate limiting for the API endpoints
5. Regular security updates for dependencies

### Monitoring and Maintenance

1. Logs are stored in the `logs` directory
2. Monitor the application using the logging output
3. Regularly backup the model files
4. Keep dependencies updated

### Troubleshooting

Common issues and solutions:

1. If the application fails to start:
   - Check if all dependencies are installed
   - Verify the model files exist in the correct location
   - Check the logs for specific error messages

2. If predictions fail:
   - Verify the model files are not corrupted
   - Check the input data format
   - Review the logs for error details

3. Performance issues:
   - Check the number of workers in gunicorn.conf.py
   - Monitor system resources
   - Consider scaling options if needed

For more detailed information about specific deployment platforms or issues, please consult the documentation or raise an issue in the repository.