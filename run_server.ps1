# Activate virtual environment if it exists
if (Test-Path ".\venv\Scripts\Activate.ps1") {
    . .\venv\Scripts\Activate.ps1
}

# Install requirements if not already installed
if (!(Test-Path ".\venv\Lib\site-packages\waitress")) {
    Write-Host "Installing requirements..."
    pip install -r requirements.txt
}

# Run the application using Waitress
Write-Host "Starting server on http://localhost:8000"
python -c "from waitress import serve; from wsgi import application; serve(application, host='0.0.0.0', port=8000)"
