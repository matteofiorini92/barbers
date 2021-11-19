from django import forms
from .models import Barber, Treatment, Booking
from django.forms import DateField, TimeField, widgets


class BarberForm(forms.ModelForm):

    class Meta:
        model = Barber
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False)


class TreatmentForm(forms.ModelForm):

    class Meta:
        model = Treatment
        fields = '__all__'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'date': widgets.DateInput(attrs={'type': 'date'}),
            'time': widgets.TimeInput(attrs={'type': 'time'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
