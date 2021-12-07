from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('<int:treatment_id>/<int:barber_id>/<int:availability_id>/', views.checkout, name='checkout'),
    path('checkout-success/<int:reservation_id>', views.checkout_success, name='checkout_success'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
