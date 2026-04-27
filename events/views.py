from django.shortcuts import render, redirect
from django.http import HttpResponse
from events.forms import EventModelForm
from events.models import Event
from django.contrib import messages
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


#Froms

def create_event(request):
    # form = EventForm()
    form = EventModelForm()
    if request.method == 'POST':
        form = EventModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Added Successfully")
            return redirect('create-event')
            # data = form.cleaned_data
            # name = data.get('name')
            # description = data.get('description')
            # date = data.get('date')
            # time = data.get('time')
            # location = data.get('location')
            # catagory = data.get('catagory')

            # event = Event.objects.create(name=name, description=description, date=date, time = time, location = location, catagory = catagory)
            # # return HttpResponse("Event submitted successfully.")
        return render(request, 'dashboard/create_event.html', {'form': form})

    
    context = {
        "form" : form
    }
    return render(request, "dashboard/create_event.html", context)