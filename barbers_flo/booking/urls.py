from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_booking_1, name='new_booking_1'),
    path('booking/<int:treatment_id>/', views.new_booking_2, name='new_booking_2'),
]