from django.shortcuts import render

# Create your views here.

def test_event(request):
    return render(request, "dashboard/dashboard.html")

def home(request):
    return render(request, "dashboard/homepage.html")

def eventlist(request):
    return render(request, "dashboard/eventlist.html")
    
def event_details(request):
    return render(request, "dashboard/event_details.html")

def user_dashboard(request):
    return render(request, "dashboard/user_dashboard.html")