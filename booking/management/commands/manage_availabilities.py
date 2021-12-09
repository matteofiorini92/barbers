from django.core.management.base import BaseCommand, CommandError
from .models import Availability
from management.models import Barber
from datetime import date, datetime, timedelta
from calendar import monthrange


class Command(BaseCommand):

    # https://stackoverflow.com/a/1060330/16735714
    def daterange(start_date, end_date):
        for n in range(int((end_date - start_date).days)):
            yield start_date + timedelta(n)


    # adapt above view to iterate through 30 minutes delta
    def timerange(start_time, end_time):
        for n in range(int((end_time - start_time).seconds/1800)):
            delta = 30 * n
            yield start_time + timedelta(minutes=delta)


    def make_availabilities():
        """ A view to create new slots for the end of the calendar """
        last_available_day = Availability.objects.all().order_by('-date')[:1][0].date
        today = date.today()
        days_curr_month = monthrange(today.year, today.month)[1]
        one_month_from_now = today + timedelta(days=days_curr_month)
        barbers = Barber.objects.all()

        if (last_available_day != one_month_from_now or not last_available_day):
            for single_date in daterange(last_available_day, one_month_from_now + timedelta(days=1)):
                if single_date.weekday() != 5 and single_date.weekday() != 6:
                    for barber in barbers:
                        start_time = datetime.strptime(str(single_date) + " " + str(barber.start_time), '%Y-%m-%d %H:%M:%S')
                        end_time = datetime.strptime(str(single_date) + " " + str(barber.end_time), '%Y-%m-%d %H:%M:%S')
                        for thirty_minutes in timerange(start_time, end_time):
                            slot = Availability(barber=barber, date=thirty_minutes.date(), time=thirty_minutes.time(), available=True)
                            slot.save()


    def clean_up_availabilities():
        """ A view to delete availability for past dates """
        oldest_available_date = Availability.objects.all().order_by('date')[:1][0].date
        today = date.today()
        if oldest_available_date < today:
            availabilities = Availability.objects.all().order_by('date')
            for availability in availabilities:
                if availability.date < today:
                    availability.delete()
                else:
                    break

    def handle(self):
        clean_up_availabilities()
        make_availabilities()
        return
