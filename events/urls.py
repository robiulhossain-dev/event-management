from django.urls import path
from events.views import test_event,home, eventlist, event_details, user_dashboard, create_event, update_event, delete_event

urlpatterns = [
    path('test-event/', test_event),
    path('home/', home, name = 'home'),
    path('event-list/', eventlist, name='event-list'),
    path('event-details/', event_details, name='event-details'),
    path('user-dashboard/', user_dashboard, name='user-dashboard'),
    path('create-event/', create_event, name='create-event'),
    path('update-event/<int:id>/', update_event, name='update-event'),
    path('delete-event/<int:id>/', delete_event, name='delete-event'),
]