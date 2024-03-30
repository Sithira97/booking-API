from django import forms
from .models import Booking
from django.contrib.auth.models import User
import datetime


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    date_of_reservation = forms.DateField(initial=datetime.date.today, widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = "__all__"