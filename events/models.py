from django.db import models

# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=100)
    catagory = models.ForeignKey(
        "Catagory",
        on_delete=models.CASCADE)




class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    event = models.ManyToManyField(Event)


class Catagory(models.Model): 
    CATAGORY_NAME = (
        ('sports' , 'Sports'),
        ('music' , 'Music'),
        ('festival' , 'Festival'), 
        ('cultural' , 'Cultural'),
        ('bussiness' , 'Bussiness'),
        ('tech' , 'Tech'),
        ('gaming' , 'Gaming'),
    )
    name = models.CharField(max_length=50, choices = CATAGORY_NAME, unique = True)
    description = models.TextField()

    def __str__(self):
        return self.name


# Event.objects.create(e_name = "Istanbul Wine Party", e_description = "Lorem ipsum dollor site amet the best consectuer diam adipiscing elites sed diam nonummy nibh the euismod tincidunt ut laoreet dolore magna aliquam erat volutpat insignia the consectuer adipiscing elit", e_date = "2026-12-12", e_time = "10:30", e_location = "Taskim Square, Istanbul, Turkiye", 