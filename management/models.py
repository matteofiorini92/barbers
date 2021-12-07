from django.db import models

# Create your models here.


class Treatment(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField(null=False, blank=False)
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
