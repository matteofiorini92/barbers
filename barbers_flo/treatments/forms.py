from django.forms import ModelForm, Textarea
from .models import Treatment


# Create the form class.
class TreatmentForm(ModelForm):
    class Meta:
        model = Treatment
        fields = '__all__'
        widgets = {
            'description': Textarea(attrs={'rows': 5}),
        }
