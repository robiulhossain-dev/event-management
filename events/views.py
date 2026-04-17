from django.shortcuts import render

# Create your views here.

def test_event(request):
    return render(request, "dashboard/dashboard.html")

