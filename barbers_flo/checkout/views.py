from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from booking.models import Availability
from management.models import Treatment, Barber
from .forms import ReservationForm

import stripe

# Create your views here.


def checkout(request, treatment_id, day, barber_id, availability_id):
    treatment = get_object_or_404(Treatment, id=treatment_id)
    barber = get_object_or_404(Barber, id=barber_id)
    availability = get_object_or_404(Availability, id=availability_id)
    form = ReservationForm(initial={'treatment': treatment, 'barber': barber, 'date': day, 'time': availability.time, 'duration': treatment.duration, 'order_total': treatment.price})
    # https://stackoverflow.com/questions/50934156/how-to-disable-a-field-in-crispy-form-django
    form.fields['treatment'].disabled = True
    form.fields['barber'].disabled = True
    form.fields['date'].disabled = True
    form.fields['time'].disabled = True
    form.fields['duration'].disabled = True
    form.fields['order_total'].disabled = True
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    total = treatment.price
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY
    )
    if request.method == 'POST':
        slots = int(treatment.duration.seconds/60/30)
        for slot in range(1, slots + 1):
            Availability.objects.filter(id=availability_id).update(available=False)
            availability_id += 1
    print(intent)
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
        'treatment': treatment,
        'barber': barber,
        'availability': availability,
        'form': form
    }
    return render(request, template, context)
