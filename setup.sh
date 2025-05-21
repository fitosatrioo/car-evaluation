#!/bin/bash

echo "Setting up Car Evaluation Application environment..."

# Create virtual environment
echo "Creating Python virtual environment..."
python3 -m venv venv

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing required packages..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Environment setup complete!"
echo "To activate this environment in the future, run:"
echo "source venv/bin/activate"
echo ""
echo "To start the Flask application, run:"
echo "python app.py"
echo ""
echo "For development with auto-reload, use:"
echo "FLASK_APP=app.py FLASK_ENV=development flask run"
echo ""
echo "For Jupyter notebook analysis, run:"
echo "jupyter notebook car.ipynb"