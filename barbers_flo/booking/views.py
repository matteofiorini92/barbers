from django.shortcuts import render

# Create your views here.


def booking(request):
    """ A view to return the booking page """
    return render(request, 'booking/new_booking.html')
