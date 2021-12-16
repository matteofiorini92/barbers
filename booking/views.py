from django.shortcuts import render, get_object_or_404
from .models import Availability
from datetime import date, datetime, timedelta
from calendar import monthrange
from management.models import Treatment, Barber

# Create your views here.


def new_booking_1(request):
    """ A view to return the first step of
        the booking page (select treatment) """
    treatments = Treatment.objects.all().order_by('name')
    template = 'booking/new_booking_1.html'
    context = {
        'treatments': treatments,
    }
    return render(request, template, context)

# https://stackoverflow.com/a/1060330/16735714


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

# adapt above view to iterate through 30 minutes delta


def timerange(start_time, end_time):
    for n in range(int((end_time - start_time).seconds/1800)):
        delta = 30 * n
        yield start_time + timedelta(minutes=delta)


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
    for single_date in daterange(first_day_curr_month, last_day_next_month +
                                 timedelta(days=1)):
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
    barbers = Barber.objects.all().order_by('barber_name')
    template = 'booking/new_booking_3.html'
    context = {
        'treatment': treatment,
        'day': day,
        'barbers': barbers,
    }
    return render(request, template, context)


def new_booking_4(request, treatment_id, day, barber_id):
    """ A view to return the third fourth of the booking page (select time) """
    treatment = get_object_or_404(Treatment, id=treatment_id)
    barber = get_object_or_404(Barber, id=barber_id)
    availabilities = Availability.objects.filter(
                                                 barber=barber,
                                                 date=day
                                                ).order_by('time')
    slots = int(treatment.duration.seconds/60/30)
    for availability in availabilities:
        available = True
        availability_id = availability.id
        for slot in range(1, slots + 1):
            if not Availability.objects.get(id=availability_id).available:
                available = False
                break
            availability_id += 1
        if available:
            availability.available = True
        else:
            availability.available = False
    template = 'booking/new_booking_4.html'
    context = {
        'treatment': treatment,
        'day': day,
        'barber': barber,
        'availabilities': availabilities,
    }
    return render(request, template, context)
