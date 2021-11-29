from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:treatment_id>/<str:day>/<int:barber_id>/<int:availability_id>/', views.checkout, name='checkout'),
    path('wh/', webhook, name='webhook'),
]
