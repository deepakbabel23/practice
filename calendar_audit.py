from time import timezone
import dateutil.parser
import datetime
from datetime import datetime, timedelta
import os.path
from dateutil.relativedelta import relativedelta

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from collections import Counter

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
ONE = 1
THREE = 3
num_months = ONE
audit_events = []

def get_calendar_date(frm, to):
    from_month = datetime.today() - relativedelta(months=frm)
    n_months_ago = from_month - relativedelta(months=to)
    tmin = n_months_ago.isoformat('T') + "Z"
    tmax = from_month.isoformat('T') + "Z"
    return (tmin,tmax)

def get_meeting_duration(start, end, all_day_event):
    duration = None
    if all_day_event:
        duration = 24*60
    else:
        tmp_duration = str(dateutil.parser.isoparse(end) - dateutil.parser.isoparse(start))
        hrs, mins, secs = tmp_duration.split(":")
        duration = abs(int(hrs) * 60 - int(mins))
    return duration

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        #print("token file exists")
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        service1 = build('calendar', 'v3', credentials=creds)        
        calendar = service.calendars().get(calendarId='primary').execute()
        calendar_id = calendar["id"]
        # Call the Calendar API        
        #print('Getting the upcoming events')
        
        months = []
        events_result = []
        for month in range(0,THREE):
            tmin, tmax = get_calendar_date(month,num_months)
            
            event_result = service.events().list(calendarId='primary', singleEvents=True,
                                              timeMin = tmin, timeMax= tmax, orderBy='startTime').execute()
            events = event_result.get('items', [])
            if not events:
                print('No upcoming events found in this month {}.'.format(month+1))
                continue
            months.append((tmin,tmax))
            events_result.append(events)
        months_data = []
        total_duration = 0
        max_meeting_month = 0
        max_meeting_month_index = 0
        min_meeting_month = 0
        min_meeting_month_index = 0
        attendees_cntr = Counter()
        for index, events in enumerate(events_result):
            month_duration = 0            
            eventSet = set()
            all_day_event = False
            for event in events:
                attendee_list = []
                all_day_event = False
                start = event['start'].get('dateTime', event['start'].get('date'))
                if event['start'].get('dateTime') is None:
                    all_day_event = True
                end = event['end'].get('dateTime', event['end'].get('date'))
                instances = None
                tmp_eventId = None
                tmp_eventId = event.get('recurringEventId')
                num_occurrences = 0
                #recurrent = False
                attendees = event.get('attendees')
                if attendees is not None and len(attendees) > 1:                    
                    for attendee in attendees:
                        if attendee.get("self") is None:
                            attendee_list.append(attendee["email"])
                            attendees_cntr.update({attendee["email"]:1})
                if tmp_eventId is not None:
                    if(tmp_eventId not in eventSet):                        
                        instances = service.events().instances(calendarId='primary', eventId=tmp_eventId).execute()
                        num_occurrences = len(instances['items'])
                        #recurrent = True  
                        eventSet.add(tmp_eventId)
                print("Meeting details: ",event['summary'])
                if instances is not None:                    
                    month_duration += num_occurrences*get_meeting_duration(start,end,all_day_event)
                else:
                    month_duration += get_meeting_duration(start,end,all_day_event)            
            months_data.append(month_duration)
            total_duration += month_duration
            max_meeting_month = max(max_meeting_month,month_duration)
            if index != 0:
                min_meeting_month = min(min_meeting_month,month_duration)
            else:
                min_meeting_month = month_duration
            if max_meeting_month == month_duration:
                max_meeting_month_index = index
            if min_meeting_month == month_duration:
                min_meeting_month_index = index
        print("\n")
        print("***********************Per Month Duration matrix*******************")
        for ind, month_data in enumerate(months_data):
            print("Total time spent in meetings in {}th months is = {}".format(ind+1,month_data))        
        print("***********************3 Months Duration matrix*******************")
        print("Total time spent in meetings in 3 months is = {}".format(total_duration))
        print("\n*****************Maximum vs minimum meeting time Months data******")
        print("Maximum time was spent in {}th month in meetings amongst last 3 months ".format(max_meeting_month_index))        
        print("Minimum time was spent in {}th month in meetings amongst last 3 months ".format(min_meeting_month_index))
        print("\n**************Most common collaborators data**********************")
        most_common_attendees = attendees_cntr.most_common(3)
        print("Maximum time was spent with these 3 people :{}".format(most_common_attendees))

    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__=="__main__":
    main()