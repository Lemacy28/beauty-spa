from django import forms
from .models import Service, Booking



class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['name', 'description', 'price']

class BookingForm(forms.ModelForm):
    date = forms.DateTimeField(widget=forms.TextInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Booking
        fields = ['service', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }



