import os

class Config:
    SECRET_KEY = 'secret-key' #os.environ.get('SECRET_KEY')
    UPLOAD_FOLDER = 'uploads'  # Directory to store uploaded CSV files
    FILTER_FOLDER= "edited"
    SHEETS_JSON = "key.json"
