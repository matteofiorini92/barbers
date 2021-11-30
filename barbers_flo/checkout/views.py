from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.views.decorators.http import require_POST
# from django.contrib import messages
from booking.models import Availability
from management.models import Treatment, Barber
from .forms import ReservationForm
from .models import Reservation


import stripe

# Create your views here.

@require_POST
def cache_checkout_data(request):
    pid = request.POST.get('client_secret').split('_secret')[0]
    stripe.api_key = settings.STRIPE_SECRET_KEY
    stripe.PaymentIntent.modify(pid, metadata={
        'username': request.user,
    })
    return HttpResponse(status=200)


def checkout(request, treatment_id, barber_id, availability_id):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    treatment = get_object_or_404(Treatment, id=treatment_id)
    barber = get_object_or_404(Barber, id=barber_id)
    availability = get_object_or_404(Availability, id=availability_id)
    form = ReservationForm(initial={'treatment': treatment, 'barber': barber, 'date': availability.date, 'time': availability.time, 'duration': treatment.duration, 'order_total': treatment.price})
    # https://stackoverflow.com/questions/50934156/how-to-disable-a-field-in-crispy-form-django
    form.fields['treatment'].disabled = True
    form.fields['barber'].disabled = True
    form.fields['date'].disabled = True
    form.fields['time'].disabled = True
    form.fields['duration'].disabled = True
    form.fields['order_total'].disabled = True

    if request.method == 'POST':
        form_data = {
            'treatment': treatment_id,
            'barber': barber_id,
            'date': availability.date,
            'duration': treatment.duration,
            'time': availability.time,
            'order_total': treatment.price,
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
        }

        reservation_form = ReservationForm(form_data)
        if reservation_form.is_valid():
            reservation = reservation_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            reservation.stripe_pid = pid
            # reservation.user_profile = request.user
            # order.original_bag = json.dumps(bag)
            reservation.save()
            return redirect('checkout_success', reservation.id)
        # else:
            # messages.error(request, ("Error message here."))
    else:
        total = treatment.price
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        # make slots unavailable
        slots = int(treatment.duration.seconds/60/30)
        for slot in range(1, slots + 1):
            Availability.objects.filter(id=availability_id).update(available=False)
            availability_id += 1

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


def checkout_success(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)
    # messages.success(request, f'Reservation confirmed! Your reservation number is { reservation_id }')
    template = 'checkout/checkout-success.html'
    context = {
        'reservation': reservation
    }
    return render(request, template, context)