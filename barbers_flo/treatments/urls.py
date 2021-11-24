from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_treatment, name='new_treatment'),
    path('get_treatment/', views.get_treatment, name='get_treatment'),
    path('edit_treatment/', views.edit_treatment, name='edit_treatment'),
]
