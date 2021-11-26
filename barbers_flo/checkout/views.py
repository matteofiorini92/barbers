from django.shortcuts import render, redirect
from django.conf import settings

import stripe

# Create your views here.


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    total = 100.00
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    print(intent)
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret
    }
    return render(request, template, context)
