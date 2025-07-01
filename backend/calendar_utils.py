# Google Calendar Service Account Integration
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime, os

SERVICE_ACCOUNT_FILE = os.getenv("SERVICE_ACCOUNT_FILE", "service_account.json")
SCOPES = ['https://www.googleapis.com/auth/calendar']

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)
service = build("calendar", "v3", credentials=credentials)
CALENDAR_ID = os.getenv("CALENDAR_ID")

def check_availability():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    events_result = service.events().list(calendarId=CALENDAR_ID, timeMin=now, maxResults=5).execute()
    events = events_result.get('items', [])
    return events

def book_appointment(start_time, end_time, summary):
    event = {
        'summary': summary,
        'start': {'dateTime': start_time, 'timeZone': 'UTC'},
        'end': {'dateTime': end_time, 'timeZone': 'UTC'}
    }
    service.events().insert(calendarId=CALENDAR_ID, body=event).execute()
