from django.urls import path
from events.views import test_event,home, eventlist, event_details, user_dashboard, create_event

urlpatterns = [
    path('test-event/', test_event),
    path('home/', home),
    path('event-list/', eventlist),
    path('event-details/', event_details),
    path('user-dashboard/', user_dashboard),
    path('create-event/', create_event, name='create-event'),
]