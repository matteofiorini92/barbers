from django.contrib import admin
from .models import Reservation

# Register your models here.

class ReservationAdmin(admin.ModelAdmin):
    list_display = (
        'user_profile',
        'barber',
        'treatment',
        'order_total',
        'stripe_pid'
)


admin.site.register(Reservation, ReservationAdmin)
