import os
import logging
from datetime import datetime, timedelta, timezone
from google.oauth2 import service_account
from googleapiclient.discovery import build
from config import Config

logger = logging.getLogger(__name__)

class GoogleCalendarService:
    def __init__(self):
        self.service = None
        self.calendar_id = 'primary'
        self._initialize_service()

    def _initialize_service(self):
        try:
            credentials_file = Config.GOOGLE_CALENDAR_CREDENTIALS_FILE
            if os.path.exists(credentials_file):
                self.credentials = service_account.Credentials.from_service_account_file(
                    credentials_file, scopes=Config.GOOGLE_CALENDAR_SCOPES
                )
                self.service = build('calendar', 'v3', credentials=self.credentials)
                logger.info("Google Calendar service initialized")
            else:
                logger.warning("Credentials file not found")
        except Exception as e:
            logger.error(f"Failed to initialize Calendar service: {str(e)}")

    def is_available(self):
        return self.service is not None

    def create_event(self, event_data):
        if not self.is_available():
            return None
        try:
            google_event = {
                'summary': event_data.get('title', 'AI Scheduled Task'),
                'description': event_data.get('description', ''),
                'start': {'dateTime': event_data['start_time'], 'timeZone': Config.TIMEZONE},
                'end': {'dateTime': event_data['end_time'], 'timeZone': Config.TIMEZONE}
            }
            created_event = self.service.events().insert(
                calendarId=self.calendar_id, body=google_event
            ).execute()
            return {'id': created_event.get('id')}
        except Exception as e:
            logger.error(f"Error creating calendar event: {str(e)}")
            return None
