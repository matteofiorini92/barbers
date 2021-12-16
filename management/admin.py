from django.contrib import admin
from .models import Treatment, Barber

# Register your models here.


class BarberAdmin(admin.ModelAdmin):
    list_display = (
        'barber_name',
        'start_time',
        'end_time',
        'profile_picture',
    )

    ordering = ('barber_name',)


class TreatmentAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
        'price',
        'duration',
        'picture',
    )


admin.site.register(Barber, BarberAdmin)
admin.site.register(Treatment, TreatmentAdmin)
