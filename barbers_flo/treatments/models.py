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