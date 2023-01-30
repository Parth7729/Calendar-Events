For run this project on a local machine:

```pip install - r requriments.txt```

- Endpoint:

```/rest/v1/calendar/init/ -> GoogleCalendarInitView()```

This view should start step 1 of the OAuth. Which will prompt user for his/her credentials

```/rest/v1/calendar/redirect/ -> GoogleCalendarRedirectView()```

This view will do two things

- Handle redirect request sent by google with code for token. You need to implement mechanism to get access_token from given code
- Once got the access_token get list of events in users calendar
