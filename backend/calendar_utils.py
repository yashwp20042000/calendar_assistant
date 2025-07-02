# Google Calendar Service Account Integration
from google.oauth2 import service_account
from googleapiclient.discovery import build
import datetime, os
from dotenv import load_dotenv
import json 
from google.oauth2 import service_account

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/calendar"]
service_account_info = json.loads(os.getenv("SERVICE_ACCOUNT_JSON"))
service_account_info["private_key"] = service_account_info["private_key"].replace("\\n", "\n")

credentials = service_account.Credentials.from_service_account_info(
    service_account_info, scopes=SCOPES
)

credentials = service_account.Credentials.from_service_account_info(
    service_account_info, scopes=SCOPES
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
