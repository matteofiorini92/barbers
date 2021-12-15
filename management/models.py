from django.db import models
from datetime import timedelta, time

# Create your models here.


class Treatment(models.Model):
    class TreatmentDurations(timedelta, models.Choices):
        THIRTY_MINUTES = 0, 1800, 0, '30 minutes'
        ONE_HOUR = 0, 3600, 0, '1 hour'
        ONE_HOUR_AND_A_HALF = 0, 5400, 0, '1 hour and 1/2'
        TWO_HOURS = 0, 7200, 0, '2 hours'
        TWO_HOURS_AND_A_HALF = 0, 9000, 0, '2 hours and 1/2'
        THREE_HOURS = 0, 10800, 0, '3 hours'
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField(null=False, blank=False, choices=TreatmentDurations.choices, default=TreatmentDurations.THIRTY_MINUTES)
    picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Barber(models.Model):
    class BarberStartTimes(time, models.Choices):
        EIGHT_OCLOCK = 8, 00, 0, '08:00'
        EIGHT_THIRTY = 8, 30, 0, '08:30'
        NINE_OCLOCK = 9, 00, 0, '09:00'
        NINE_THIRTY = 9, 30, 0, '09:30'
        TEN_OCLOCK = 10, 00, 0, '10:00'
        TEN_THIRTY = 10, 30, 0, '10:30'
        ELEVEN_OCLOCK = 11, 00, 0, '11:00'
        ELEVEN_THIRTY = 11, 30, 0, '11:30'
        TWELVE_OCLOCK = 12, 00, 0, '12:00'
        TWELVE_THIRTY = 12, 30, 0, '12:30'
        ONE_OCLOCK = 13, 00, 0, '13:00'
        ONE_THIRTY = 13, 30, 0, '13:30'
        TWO_OCLOCK = 14, 00, 0, '14:00'
    class BarberEndTimes(time, models.Choices):
        TWELVE_OCLOCK = 12, 00, 0, '12:00'
        TWELVE_THIRTY = 12, 30, 0, '12:30'
        ONE_OCLOCK = 13, 00, 0, '13:00'
        ONE_THIRTY = 13, 30, 0, '13:30'
        TWO_OCLOCK = 14, 00, 0, '14:00'
        TWO_THIRTY = 14, 30, 0, '14:30'
        THREE_OCLOCK = 15, 00, 0, '15:00'
        THREE_THIRTY = 15, 30, 0, '15:30'
        FOUR_OCLOCK = 16, 00, 0, '16:00'
        FOUR_THIRTY = 16, 30, 0, '16:30'
        FIVE_OCLOCK = 17, 00, 0, '17:00'
        FIVE_THIRTY = 17, 30, 0, '17:30'
        SIX_OCLOCK = 18, 00, 0, '18:00'
    barber_name = models.CharField(max_length=254)
    start_time = models.TimeField(null=False, blank=False, choices=BarberStartTimes.choices, default=BarberStartTimes.EIGHT_OCLOCK)
    end_time = models.TimeField(null=False, blank=False, choices=BarberEndTimes.choices, default=BarberEndTimes.FIVE_OCLOCK)
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.barber_name
