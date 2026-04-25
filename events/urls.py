from django.urls import path
from events.views import test_event,home, eventlist, event_details, user_dashboard

urlpatterns = [
    path('test-event/', test_event),
    path('home/', home),
    path('event-list/', eventlist),
    path('event-details/', event_details),
    path('user-dashboard/', user_dashboard),
]