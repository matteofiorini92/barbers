from django.contrib import admin
from .models import Barber, Treatment, Booking, Availability

# Register your models here.


class BarberAdmin(admin.ModelAdmin):
    list_display = (
        'barber_name',
        'profile_picture',
        'start_time',
        'end_time',
    )

    ordering = ('barber_name',)


class TreatmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'duration',
    )


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'barber',
        'treatment',
        'customer_name',
        'date',
        'time',
    )


class AvailabilityAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'barber',
        'date',
        'time',
        'available'
)


admin.site.register(Barber, BarberAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Availability, AvailabilityAdmin)
