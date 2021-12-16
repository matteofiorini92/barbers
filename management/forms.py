from django.forms import ModelForm, Textarea
from .models import Treatment, Barber


# Create the form class.


class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'rows': 5}),
        }


class BarberForm(ModelForm):
    class Meta:
        model = Barber
        fields = '__all__'
