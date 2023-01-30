from django.urls import path
from .views import *

urlpatterns = [
    path('v1/calendar/init/', GoogleCalendarInitView, name='google_request'),
    path('v1/calendar/redirect/', GoogleCalendarRedirectView, name='google_redirect')
]