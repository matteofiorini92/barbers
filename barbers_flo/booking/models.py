from django.db import models

# Create your models here.


class Barber(models.Model):
    barber_name = models.CharField(max_length=254)
    profile_picture = models.ImageField(null=True, blank=True)
    start_time = models.TimeField(default='08:00:00')
    end_time = models.TimeField(default='17:00:00')

    def __str__(self):
        return self.barber_name


class Treatment(models.Model):
    name = models.CharField(max_length=254)
    description = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    duration = models.DurationField(null=False, blank=False)

    def __str__(self):
        return self.name


class Booking(models.Model):
    barber = models.ForeignKey('Barber', null=False, blank=False,
                                 on_delete=models.PROTECT)
    treatment = models.ForeignKey('Treatment', null=False, blank=False,
                                 on_delete=models.PROTECT)
    customer_name = models.CharField(max_length=254)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)


class Availability(models.Model):
    class Meta:
        verbose_name_plural = 'Availabilities'
    barber = models.ForeignKey('Barber', null=False, blank=False,
                                 on_delete=models.PROTECT)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    available = models.BooleanField(default=True)