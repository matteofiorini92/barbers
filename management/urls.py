from django.urls import path
from . import views

urlpatterns = [
    path('new_treatment/', views.new_treatment, name='new_treatment'),
    path('get_treatment/', views.get_treatment, name='get_treatment'),
    path('edit_treatment/', views.edit_treatment, name='edit_treatment'),
    path('delete_treatment/<int:treatment_id>/', views.delete_treatment, name='delete_treatment'),
    path('new_barber/', views.new_barber, name='new_barber'),
    path('get_barber/', views.get_barber, name='get_barber'),
    path('edit_barber/', views.edit_barber, name='edit_barber'),
    path('delete_barber/<int:barber_id>/', views.delete_barber, name='delete_barber'),
]
