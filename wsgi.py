import os
from app import CarEvaluationApp

# Set the base directory for relative paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Create the application instance
app = CarEvaluationApp()
application = app.app  # For WSGI servers
