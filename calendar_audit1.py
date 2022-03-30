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

class CurrentMonth:
    def _init_(self):
        self._start = datetime.today()
    
    def set_end_period(self, num_months):
        self._end = self._start + relativedelta(months=num_months)

def get_calendar_date(frm, to):
    from_month = datetime.today() - relativedelta(months=frm)
    n_months_ago = from_month - relativedelta(months=to)
    tmin = n_months_ago.isoformat('T') + "Z"
    tmax = from_month.isoformat('T') + "Z"
    return (tmin,tmax)

def display_instance_date_info(event_id, calendar_id, start, end, recurrent, all_day_event, recurr_event_id, items, attendee_list=[]):
    for item in items:
        start_time = datetime.strptime(item["start"]["dateTime"].split('+')[0], '%Y-%m-%dT%H:%M:%S')
        start_time += timedelta(days=1)
        end_time = datetime.strptime(item["end"]["dateTime"].split('+')[0], '%Y-%m-%dT%H:%M:%S')
        print(item["start"]["dateTime"])
        print(item["end"]["dateTime"])
        print(start_time > end_time)
        yield AuditEvent(recurr_event_id, calendar_id, start, end, recurrent, all_day_event, attendee_list)
    

def compare_start_dates(first_date, second_date):
    first_date = { 
        "start": { "dateTime" : "2022-06-13T16:00:00+05:30", "timezone": "Asia/Kolkata"}, 
        "end": { "dateTime" : "2022-06-13T17:00:00+05:30", "timezone": "Asia/Kolkata"}
                 }
    second_date = { 
        "start": { "dateTime" : "2022-07-13T16:00:00+05:30", "timezone": "Asia/Kolkata"}, 
        "end": { "dateTime" : "2022-07-13T17:00:00+05:30", "timezone": "Asia/Kolkata"}
                 }
    first = datetime.strptime(first_date["start"]["dateTime"].split('+')[0], '%Y-%m-%dT%H:%M:%S')
    second = datetime.strptime(second_date["start"]["dateTime"].split('+')[0], '%Y-%m-%dT%H:%M:%S')
    print(first < second)

class AuditEvent:
    def __init__(self, id, calendar_id, start, end, recurrent, all_day_event=False, attendee_list = []):
        self._event_id = id
        self._start = dateutil.parser.isoparse(start)
        self._end = dateutil.parser.isoparse(end)
        if all_day_event:
            self._duration = 24*60;
        else:
            self.set_duration(start,end)        
        self._calendar_id = calendar_id        
        self._single, self._recurrent = (False, True) if recurrent else (True, False)
        self.set_attendees(attendee_list)
        #self._current_month = CurrentMonth().get_month(self._start, self._end)

    def set_duration(self, start, end):
        tmp_duration = str(self._end - self._start)
        hrs, mins, secs = tmp_duration.split(":")
        self._duration = abs(int(hrs) * 60 - int(mins))
        print(self._duration)
    
    def set_attendees(self, attendees):
        self._attendees = attendees

    def get_calendar_id(self):
        """ Get the meeting's calendar id"""
        return self._calendar_id

    def get_meeting_duration(self):
        """ Get the meeting duration in hours"""
        return self._duration
        """
        single occurrence = endTime - startTime
        recurring meeting = (endTime - startTime) * (no of times meeting was repeated/end date/infinite)
        recurring meeting - repeat frequency - daily/weekly/monthly/yearly
        """
        pass

    def get_attendees(self):
        """ Get the meeting attendees"""
        return self._attendees

    def calculate_meeting_duration_per_day(event_id):
        """ Get the meeting duration"""
        pass

    def calculate_meeting_duration_per_week(event_id):
        """ Get the meeting duration"""
        pass

    def calculate_meeting_duration_per_month(event_id):
        """ Get the meeting duration"""
        pass

    def m1():
        """This method would return the total time spent per month for last 3 months"""
        """
        return get_meetings_total_duration_per_month
        else return get_meetings_total_duration_per_week * 4
        else return get_meetings_total_duration_per_day * number_of_days_in_month
        """
        pass

    def m2():
        """This method would return which months had highest/least number of meetings"""
        pass

    def m3():
        """This method would return the top 3 people who were meeting collaborators"""
        pass

    def m4():
        """This method would return the total time spent in conducting/recruiting for interviews"""
        pass

def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        print("token file exists")
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
        #now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        print('Getting the upcoming events')
        
        months = []
        events_result = []
        for month in range(0,THREE):
            tmin, tmax = get_calendar_date(month,num_months)
            
            event_result = service.events().list(calendarId='primary', singleEvents=True,
                                              timeMin = tmin, timeMax= tmax, orderBy='startTime').execute()
            events = event_result.get('items', [])
            if not events:
                print('No upcoming events found.')
                continue
            months.append((tmin,tmax))
            events_result.append(events)
        
        #events = events_result.get('items', [])
        total_duration = 0
        max_meeting_month = 0
        max_meeting_month_index = 0
        min_meeting_month = 0
        min_meeting_month_index = 0
        attendees_cntr = Counter()
        for index, events in enumerate(events_result):
            month_duration = 0
            # Prints the start and name of the next 10 events
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
                recurrent = False
                attendees = event.get('attendees')
                if attendees is not None and len(attendees) > 1:                    
                    for attendee in attendees:
                        if "self" not in attendee:
                            attendee_list.append(attendee["email"])
                            attendees_cntr.update({attendee["email"]:1})
                if tmp_eventId is not None:
                    if(tmp_eventId not in eventSet):
                        print(f"eventId recurring is = {tmp_eventId}")
                        instances = service.events().instances(calendarId='primary', eventId=tmp_eventId).execute()
                        num_occurrences = len(instances['items'])
                        recurrent = True
                        recur_event = display_instance_date_info(event['id'], calendar_id, start, end, recurrent, all_day_event, tmp_eventId, instances['items'])
                        for evt in recur_event:
                            audit_events.append(evt)
                            print(evt.get_meeting_duration())                        
                        print(f"number of instances of this meeting is = {num_occurrences}")
                        print("calling instances method now")
                        print("adding this event to event set",event['summary'], id(event['id']), start, end, all_day_event)
                        eventSet.add(tmp_eventId)
                #print(f"event id is = {event['id']}")
                print(start, event['summary'])                
                audit_event = AuditEvent(event['id'], calendar_id, start, end, recurrent, all_day_event, attendee_list=attendee_list)
                if instances is not None:
                    print("total duration of all meeting occurrences is = ",num_occurrences*audit_event.get_meeting_duration())
                    compare_start_dates(None, None)
                    print("*************")
                    month_duration += num_occurrences*audit_event.get_meeting_duration()                    
                else:
                    month_duration += audit_event.get_meeting_duration()                    
                audit_events.append(audit_event)
            print("***********************1 Months Duration matrix*******************")
            print("Total time spent in meetings in {}th months is = {}".format(index,month_duration))
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
        print("***********************3 Months Duration matrix*******************")
        print("Total time spent in meetings in 3 months is = {}".format(total_duration))
        print("Maximum time was spent in {}th month in meetings amongst last 3 months ".format(max_meeting_month_index))
        print("Minimum time was spent in {}th month in meetings amongst last 3 months ".format(min_meeting_month_index))
        most_common_attendees = attendees_cntr.most_common(3)
        print("Maximum time was spent with these 3 people :{}".format(most_common_attendees))

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__=="__main__":
    main()