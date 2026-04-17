from django.urls import path
from events.views import test_event

urlpatterns = [
    path('test-event/', test_event),
]