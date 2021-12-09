from django.core.management.base import BaseCommand, CommandError
from booking.models import Availability
from booking.views import daterange, timerange
from management.models import Barber
from datetime import date, datetime, timedelta
from calendar import monthrange


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            oldest_available_date = Availability.objects.all().order_by('date')[:1][0].date
            today = date.today()
            if oldest_available_date < today:
                availabilities = Availability.objects.all().order_by('date')
                for availability in availabilities:
                    if availability.date < today:
                        availability.delete()
                    else:
                        break
        except IndexError as error:
            print(error)
        """ A view to create new slots for the end of the calendar """
        try:
            last_available_day = Availability.objects.all().order_by('-date')[:1][0].date
        except IndexError as error:
            last_available_day = date.today()
        today = date.today()
        days_curr_month = monthrange(today.year, today.month)[1]
        one_month_from_now = today + timedelta(days=days_curr_month)
        print(last_available_day)
        print(today)
        print(days_curr_month)
        print(one_month_from_now)
        barbers = Barber.objects.all()

        if (last_available_day != one_month_from_now):
            for single_date in daterange(last_available_day + timedelta(days=1), one_month_from_now + timedelta(days=1)):
                print(single_date)
                if single_date.weekday() != 5 and single_date.weekday() != 6:
                    for barber in barbers:
                        start_time = datetime.strptime(str(single_date) + " " + str(barber.start_time), '%Y-%m-%d %H:%M:%S')
                        end_time = datetime.strptime(str(single_date) + " " + str(barber.end_time), '%Y-%m-%d %H:%M:%S')
                        for thirty_minutes in timerange(start_time, end_time):
                            slot = Availability(barber=barber, date=thirty_minutes.date(), time=thirty_minutes.time(), available=True)
                            slot.save()
        return
