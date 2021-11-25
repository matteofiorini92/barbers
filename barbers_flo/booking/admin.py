from django.contrib import admin
from .models import Availability

# Register your models here.

class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'barber',
        'date',
        'time',
        'available'
)


admin.site.register(Availability, AvailabilityAdmin)
