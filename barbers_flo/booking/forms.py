from django import forms
from .models import Barber, Treatment, Booking


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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        barbers = Barber.objects.all()
        treatments = Treatment.objects.all()
