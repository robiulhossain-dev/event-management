from django.db import models

# Create your models here.
class Event(models.Model):
    e_name = models.CharField(max_length=100)
    e_description = models.TextField()
    e_date = models.DateField()
    e_time = models.TimeField()
    e_location = models.CharField(max_length=100)
    e_catagory = models.ForeignKey(
        "Catagory", 
        on_delete=models.CASCADE)


class Participant(models.Model):
    p_name = models.CharField(max_length=100)
    p_email = models.EmailField(unique=True)
    p_event = models.ManyToManyField(Event)


class Catagory(models.Model):
    c_name = models.CharField(max_length=50)
    c_description = models.TextField()


# Event.objects.create(e_name = "Istanbul Wine Party", e_description = "Lorem ipsum dollor site amet the best consectuer diam adipiscing elites sed diam nonummy nibh the euismod tincidunt ut laoreet dolore magna aliquam erat volutpat insignia the consectuer adipiscing elit", e_date = "2026-12-12", e_time = "10:30", e_location = "Taskim Square, Istanbul, Turkiye", 