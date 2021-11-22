from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Treatment
from datetime import date, datetime, timedelta
from calendar import monthrange

# Create your views here.


def new_booking_1(request):
    """ A view to return the first step of the booking page (select treatment) """
    treatments = Treatment.objects.all()

    template = 'booking/new_booking_1.html'
    context = {
        'treatments': treatments,
    }
    return render(request, template, context)

# https://stackoverflow.com/a/1060330/16735714
def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def new_booking_2(request, treatment_id):
    """ A view to return the second step of the booking page (select day) """
    treatment = get_object_or_404(Treatment, id=treatment_id)
    today = date.today()
    curr_month = today.month
    first_day_curr_month = today.replace(day=1)
    days_curr_month = monthrange(today.year, today.month)[1]
    last_day_curr_month = today.replace(day=days_curr_month)
    first_day_next_month = last_day_curr_month + timedelta(days=1)
    next_month = first_day_next_month.month
    days_next_month = monthrange(first_day_next_month.year, next_month)[1]
    last_day_next_month = first_day_next_month.replace(day=days_next_month)
    # https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/

    days = []
    # https://stackoverflow.com/questions/9724906/python-date-of-the-previous-month
    for single_date in daterange(first_day_curr_month, last_day_next_month + timedelta(days=1)):
        if single_date.month == curr_month:
            if single_date.day <= today.day:
                days.append((single_date, False))
            else:
                if single_date.weekday() == 5 or single_date.weekday() == 6:
                    days.append((single_date, False))
                else:
                    days.append((single_date, True))
        else:
            if single_date.day <= today.day:
                if single_date.weekday() == 5 or single_date.weekday() == 6:
                    days.append((single_date, False))
                else:
                    days.append((single_date, True))
            else:
                days.append((single_date, False))

    template = 'booking/new_booking_2.html'
    context = {
        'treatment': treatment,
        'days': days,
    }
    return render(request, template, context)

def new_booking_3(request, treatment_id, day):
    """ A view to return the third step of the booking page (select barber) """
    treatment = get_object_or_404(Treatment, id=treatment_id)

    template = 'booking/new_booking_3.html'
    context = {
        'treatment': treatment,
        'day': day,
    }
    return render(request, template, context)