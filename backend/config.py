import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY', 'pplx-your-api-key-here')
    GOOGLE_CALENDAR_CREDENTIALS_FILE = os.getenv('GOOGLE_CREDENTIALS_FILE', 'credentials.json')
    GOOGLE_CALENDAR_SCOPES = [
        'https://www.googleapis.com/auth/calendar',
        'https://www.googleapis.com/auth/calendar.events'
    ]
    TIMEZONE = os.getenv('TIMEZONE', 'UTC')
    AI_MODEL = 'sonar-medium-online'
    AI_MAX_TOKENS = 1000
    AI_TEMPERATURE = 0.7
