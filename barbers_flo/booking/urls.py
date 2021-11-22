from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_booking_1, name='new_booking_1'),
    path('booking/<int:treatment_id>/', views.new_booking_2, name='new_booking_2'),
    path('booking/<int:treatment_id>/<str:day>', views.new_booking_3, name='new_booking_3'),
    path('booking/<int:treatment_id>/<str:day>/<int:barber_id>', views.new_booking_4, name='new_booking_4'),
]