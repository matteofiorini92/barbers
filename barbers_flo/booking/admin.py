from django.contrib import admin
from .models import Barber, Availability

# Register your models here.


class BarberAdmin(admin.ModelAdmin):
    list_display = (
        'barber_name',
        'profile_picture',
        'start_time',
        'end_time',
    )

    ordering = ('barber_name',)


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'barber',
        'date',
        'time',
        'available'
)


admin.site.register(Barber, BarberAdmin)
admin.site.register(Availability, AvailabilityAdmin)
