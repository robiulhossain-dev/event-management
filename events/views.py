from datetime import date
from django.http import HttpResponse
from events.forms import EventModelForm
from events.models import Event, Catagory
from django.contrib import messages
from django.db.models import Avg, Count, Sum, Q
from django.shortcuts import render, redirect


def test_event(request):
    return render(request, "dashboard/dashboard.html")

def home(request):
    return render(request, "dashboard/homepage.html")

def eventlist(request):
    cats = Catagory.objects.all()

    query = request.GET.get('q')
    get_cat = request.GET.get('catagory') 

    events = Event.objects.select_related('catagory').filter(date__gt=date.today()).order_by('date')

    if query:
        events = events.select_related('catagory').filter(
            Q(name__icontains=query) |
            Q(location__icontains=query)
        )

    if get_cat:
        events = events.select_related('catagory').filter(catagory_id=get_cat)

    if not query and not get_cat:
        events = events[:5]

    context = {
        'events': events,
        'cats': cats,
    }

    return render(request, "dashboard/eventlist.html", context)
    
def event_details(request):
    ev_id = request.GET.get('id')
    event = Event.objects.get(id=ev_id)
    context = {
        'event' : event
    }
    return render(request, "dashboard/event_details.html", context)



def user_dashboard(request):

    date_filter = request.GET.get('date')

    if date_filter == 'today':
        events = Event.objects.select_related('catagory').filter(date = date.today())
    elif date_filter == 'future':
        events = Event.objects.select_related('catagory').filter(date__gt = date.today())
    elif date_filter == 'past':
        events = Event.objects.select_related('catagory').filter(date__lt = date.today())
    else:
        events = Event.objects.select_related('catagory').all()

    
    counts = Event.objects.aggregate(
        total_events = Count('id'),
        today_events = Count('id', filter = Q(date=date.today())),
        future_events = Count('id', filter = Q(date__gt=date.today())),
        past_events = Count('id', filter = Q(date__lt=date.today())),
    )

    context = {
        'events' : events,
        'counts' : counts
    }

    return render(request, "dashboard/user_dashboard.html", context)


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


def update_event(request, id):

    event = Event.objects.get(id=id)
    print(event.name)
    form = EventModelForm(instance=event)

    if request.method == 'POST':
        form = EventModelForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, "Event Edited Successfully")
            return redirect('user-dashboard')

    context = {
        'form' : form,
    }

    return render(request, "dashboard/create_event.html", context)


def delete_event(request, id):
    if request.method == 'POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request,"Event Deleted Successfully")
        return redirect('user-dashboard')