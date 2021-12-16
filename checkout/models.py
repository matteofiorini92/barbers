from django.db import models
from management.models import Treatment, Barber
from profiles.models import UserProfile

# Create your models here.


class Reservation(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='reservation')
    barber = models.ForeignKey(Barber, on_delete=models.SET_NULL,
                               null=True, blank=True)
    treatment = models.ForeignKey(Treatment, on_delete=models.SET_NULL,
                                  null=True, blank=True)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    full_name = models.CharField(max_length=50, null=False,
                                 blank=False, default=None)
    email = models.EmailField(max_length=254, null=False,
                              blank=False, default=None)
    phone_number = models.CharField(max_length=20, null=False,
                                    blank=False, default=None)
    order_total = models.DecimalField(max_digits=10, decimal_places=2,
                                      null=False, default=0)
    stripe_pid = models.CharField(max_length=254, null=False, blank=False,
                                  default='')
