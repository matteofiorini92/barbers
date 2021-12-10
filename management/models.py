from django.db import models
from datetime import timedelta

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
    barber_name = models.CharField(max_length=254)
    start_time = models.TimeField(default='08:00:00')
    end_time = models.TimeField(default='17:00:00')
    profile_picture = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.barber_name
