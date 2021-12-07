from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('treatment', 'barber', 'date', 'time', 'order_total', 'full_name',
                  'email', 'phone_number')
