from django.urls import path
from events.views import test_event,home, eventlist

urlpatterns = [
    path('test-event/', test_event),
    path('home/', home),
    path('event-list/', eventlist),
]