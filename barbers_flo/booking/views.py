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


def new_booking_2(request, treatment_id):
    """ A view to return the second step of the booking page (select day) """
    treatment = get_object_or_404(Treatment, id=treatment_id)
    today = date.today()
    next_month = (today.month) + 1 if len(str((today.month) + 1)) == 2 else int("0" + str((today.month) + 1))
    # https://techoverflow.net/2019/05/16/how-to-get-number-of-days-in-month-in-python/
    last_day = monthrange(today.year, today.month)[1]
    one_month_from_now = today + timedelta(days=last_day)
    days = []
    # current month - impossible to book from beginning to current day
    for day in range(1, today.day+1):
        if len(str(day)) == 1:
            full_date = datetime.strptime(str(today.year) + "-" + str(today.month) + "-0" + str(day), '%Y-%m-%d')
        else:
            full_date = datetime.strptime(str(today.year) + "-" + str(today.month) + "-" + str(day), '%Y-%m-%d')
        days.append((full_date, False))

    # current month - available to book except for Saturdays and Sundays
    for day in range(today.day+1, last_day+1):
        if len(str(day)) == 1:
            full_date = datetime.strptime(str(today.year) + "-" + str(today.month) + "-0" + str(day), '%Y-%m-%d')
        else:
            full_date = datetime.strptime(str(today.year) + "-" + str(today.month) + "-" + str(day), '%Y-%m-%d')

        if full_date.weekday() == 5 or full_date.weekday() == 6:
            days.append((full_date, False))
        else:
            days.append((full_date, True))
    
    # next month - available to book except for Saturdays and Sundays only until same day
    for day in range(1, one_month_from_now.day+1):
        if len(str(day)) == 1:
            full_date = datetime.strptime(str(today.year) + "-" + str(next_month) + "-0" + str(day), '%Y-%m-%d')
        else:
            full_date = datetime.strptime(str(today.year) + "-" + str(next_month) + "-" + str(day), '%Y-%m-%d')

        if full_date.weekday() == 5 or full_date.weekday() == 6:
            days.append((full_date, False))
        else:
            days.append((full_date, True))
    template = 'booking/new_booking_2.html'
    context = {
        'treatment': treatment,
        'days': days,
    }
    return render(request, template, context)