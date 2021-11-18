from django.shortcuts import render
from .forms import BookingForm

# Create your views here.


def booking(request):
    """ A view to return the booking page """
    form = BookingForm()

    template = 'booking/new_booking.html'
    context = {
        'form': form,
    }
    return render(request, template, context)
