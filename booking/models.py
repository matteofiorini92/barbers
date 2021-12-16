from django.db import models

# Create your models here.


class Availability(models.Model):
    class Meta:
        verbose_name_plural = 'Availabilities'
    barber = models.ForeignKey('management.Barber', null=False, blank=False,
                               on_delete=models.CASCADE)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    available = models.BooleanField(default=True)
