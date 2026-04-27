from django import forms
from events.models import Catagory, Event, Participant

# class EventForm(forms.Form):
#     name = forms.CharField(max_length=100, label="Event Name")
#     description = forms.CharField(widget=forms.Textarea, max_length=300, label="Description")
#     date = forms.DateField(widget=forms.SelectDateWidget, label="Date")
#     time = forms.TimeField(label="Time")
#     location = forms.CharField(max_length=200, label="Location")
#     catagory = forms.ModelChoiceField(queryset=Catagory.objects.all(), label="Catagory")



class EventModelForm(forms.ModelForm):
    catagory = forms.ModelChoiceField(
        queryset=Catagory.objects.all(),
        empty_label="Select Catagory",
        widget = forms.Select(attrs={
                'class' : "border border-teal-500 w-full resize-none rounded-md placeholder:italic placeholder:text-gray-400"
            })
        )
    class Meta:
        model = Event
        fields = ['name', 'description', 'catagory', 'location', 'date', 'time' ]
        # widgets = {
        #     'date' : forms.SelectDateWidget
        # }
        widgets={
            'name' : forms.TextInput(attrs={
                'class' : "border border-teal-500 w-full rounded-md placeholder:italic placeholder:text-gray-400",
                'placeholder' : "enter event name",
            }),
            'description' : forms.Textarea(attrs={
                'class' : "border border-teal-500 w-full h-5 rows-5 resize-none rounded-md placeholder:italic placeholder:text-gray-400",
                'placeholder' : "enter event details",
                'rows': 6,
                
            }),           
            'date' : forms.SelectDateWidget(attrs={
                'class' : "border border-teal-500 resize-none rounded-md placeholder:italic placeholder:text-gray-400"
            }),
            'time' : forms.TimeInput(attrs={
                'class' : "border border-teal-500 w-fit resize-none rounded-md placeholder:italic placeholder:text-gray-400",
                'placeholder' : "hh:mm",
                
            }),
            'location' : forms.TextInput(attrs={
                'class' : "border border-teal-500 w-full rounded-md placeholder:italic placeholder:text-gray-400",
                'placeholder' : "enter event location"
            }),
            'catagory' : forms.Select(attrs={
                'class' : "border border-teal-500 w-full resize-none rounded-md placeholder:italic placeholder:text-gray-400"
            }),

        }
    