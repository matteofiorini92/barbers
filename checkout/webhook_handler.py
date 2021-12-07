from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Reservation
from booking.models import Availability
from management.models import Barber, Treatment
from profiles.models import UserProfile

from datetime import datetime
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from stripe
        """
        intent = event.data.object
        pid = intent.id
        billing_details = intent.charges.data[0].billing_details
        order_total = round(intent.charges.data[0].amount / 100, 2)
        treatment = get_object_or_404(Treatment, id=intent.charges.data[0].metadata.treatment)
        barber = get_object_or_404(Barber, id=intent.charges.data[0].metadata.barber)
        date = datetime.strptime(intent.charges.data[0].metadata.date, '%Y-%m-%d')
        user = get_object_or_404(UserProfile, user=intent.charges.data[0].metadata.username)
        # calling variable time_of_reservation to not clash with time imported on top
        time_of_reservation = datetime.strptime(intent.charges.data[0].metadata.time, '%H:%M:%S')
        availability_id = int(intent.charges.data[0].metadata.availability_id)
        reservation_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                reservation = Reservation.objects.get(
                    full_name__iexact=billing_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    date__iexact=date,
                    time__iexact=time_of_reservation,
                    # https://stackoverflow.com/questions/62673416/querytset-raised-related-field-got-invalid-lookup-iexact
                    barber__id__iexact=barber,
                    stripe_pid__iexact=pid
                )
                reservation_exists = True
                break
            except Reservation.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if reservation_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified reservation already in database',
                status=200)
        else:
            reservation = Reservation.objects.create(
                full_name=billing_details.name,
                email=billing_details.email,
                phone_number=billing_details.phone,
                treatment=treatment,
                barber=barber,
                date=date,
                time=time_of_reservation,
                order_total=order_total,
                stripe_pid=pid
            )
            # make slots unavailable
            slots = int(treatment.duration.seconds/60/30)
            for slot in range(1, slots + 1):
                Availability.objects.filter(id=availability_id).update(available=False)
                availability_id += 1
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Created reservation in webhook',
                    status=200)

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
