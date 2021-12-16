from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TreatmentForm, BarberForm
from .models import Treatment, Barber
from checkout.models import Reservation
from booking.models import Availability
from booking.views import daterange, timerange
from datetime import date, datetime, timedelta
from django.contrib import messages


def new_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TreatmentForm(initial={'price': '0.00', 'duration': 'hh:mm:ss'})

    template = 'management/new_treatment.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def get_treatment(request):
    if request.method == 'POST':
        treatment_id = int(request.POST["treatment"])
        treatment = get_object_or_404(Treatment, id=treatment_id)
        form = TreatmentForm(initial={
            'name': treatment.name,
            'description': treatment.description,
            'price': treatment.price,
            'duration': treatment.duration,
        })
    else:
        form = TreatmentForm()
        treatment_id = None
        treatment = None
    treatments = Treatment.objects.all().order_by('name')
    template = 'management/edit_treatment.html'
    context = {
        'form': form,
        'treatments': treatments,
        'treatment_id': treatment_id,
        'treatment': treatment
    }
    return render(request, template, context)


def edit_treatment(request):
    if request.method == 'POST':
        treatment = get_object_or_404(Treatment, id=request.POST["id"])
        form = TreatmentForm(request.POST, request.FILES, instance=treatment)
        if form.is_valid():
            messages.success(
                request,
                f'Treatment { treatment.name } correctly updated.'
            )
            form.save()
            form = TreatmentForm()
            treatment_id = None
            treatment = None
            treatments = Treatment.objects.all().order_by('name')
            template = 'management/edit_treatment.html'
            context = {
                'form': form,
                'treatments': treatments,
                'treatment_id': treatment_id,
                'treatment': treatment
            }
            return render(request, template, context)
    else:
        form = TreatmentForm()
    treatments = Treatment.objects.all().order_by('name')
    template = 'management/edit_treatment.html'
    context = {
        'form': form,
        'treatments': treatments
    }
    return render(request, template, context)


def delete_treatment(request, treatment_id):
    treatment = get_object_or_404(Treatment, id=treatment_id)
    treatment.delete()
    messages.success(
        request,
        f'Treatment { treatment.name } correctly deleted.'
    )
    form = TreatmentForm()
    treatment_id = None
    treatment = None
    treatments = Treatment.objects.all().order_by('name')
    template = 'management/edit_treatment.html'
    context = {
        'form': form,
        'treatments': treatments,
        'treatment_id': treatment_id,
        'treatment': treatment
    }
    return render(request, template, context)


def new_barber(request):
    if request.method == 'POST':
        form = BarberForm(request.POST, request.FILES)
        if form.is_valid():
            barber = form.save()
        """
        Creates new slots when a new barber is created
        It will only create availabilities to match the
        last available date of other barbers.
        """
        try:
            last_available_day = Availability.objects.all().order_by(
                '-date')[:1][0].date
        except IndexError:
            last_available_day = date.today()
        today = date.today()
        for single_date in daterange(
                                     today + timedelta(
                                         days=1),
                                     last_available_day + timedelta(
                                         days=1)
                                    ):
            if single_date.weekday() != 5 and single_date.weekday() != 6:
                start_time = datetime.strptime(
                    str(single_date) + " " +
                    str(barber.start_time), '%Y-%m-%d %H:%M:%S'
                )
                end_time = datetime.strptime(
                    str(single_date) + " " +
                    str(barber.end_time), '%Y-%m-%d %H:%M:%S'
                )
                for thirty_minutes in timerange(start_time, end_time):
                    slot = Availability(
                        barber=barber,
                        date=thirty_minutes.date(),
                        time=thirty_minutes.time(),
                        available=True
                    )
                    slot.save()
        return HttpResponseRedirect('/')
    else:
        form = BarberForm(
            initial={
                'start_time': '08:00:00',
                'end_time': '17:00:00'
            }
        )

    template = 'management/new_barber.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def get_barber(request):
    if request.method == 'POST':
        barber_id = int(request.POST["barber"])
        barber = get_object_or_404(Barber, id=barber_id)
        form = BarberForm(initial={
            'barber_name': barber.barber_name,
            'start_time': barber.start_time,
            'end_time': barber.end_time,
        })
    else:
        form = BarberForm()
        barber_id = None
        barber = None
    barbers = Barber.objects.all().order_by('barber_name')
    template = 'management/edit_barber.html'
    context = {
        'form': form,
        'barbers': barbers,
        'barber_id': barber_id,
        'barber': barber
    }
    return render(request, template, context)


def edit_barber(request):
    if request.method == 'POST':
        barber = get_object_or_404(Barber, id=request.POST["id"])
        form = BarberForm(request.POST, request.FILES, instance=barber)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f'Barber { barber.barber_name } correctly updated.'
            )
            form = BarberForm()
            barber_id = None
            barber = None
            barbers = Barber.objects.all().order_by('barber_name')
            template = 'management/edit_barber.html'
            context = {
                'form': form,
                'barbers': barbers,
                'barber_id': barber_id,
                'barber': barber
            }
            return render(request, template, context)
    else:
        form = BarberForm()
    barbers = Barber.objects.all()
    template = 'management/edit_barber.html'
    context = {
        'form': form,
        'barbers': barbers
    }
    return render(request, template, context)


def delete_barber(request, barber_id):
    barber = get_object_or_404(Barber, id=barber_id)
    barber.delete()
    messages.success(
        request,
        f'Barber { barber.barber_name } correctly deleted.'
    )
    form = BarberForm()
    barber_id = None
    barber = None
    barbers = Barber.objects.all().order_by('barber_name')
    template = 'management/edit_barber.html'
    context = {
        'form': form,
        'barbers': barbers,
        'barber_id': barber_id,
        'barber': barber
    }
    return render(request, template, context)


def list_of_reservations(request, day=date.today()):
    if request.method == 'POST':
        day = datetime.strptime(request.POST['day'], "%Y-%m-%d")
    reservations_list = Reservation.objects.filter(date=day).order_by('time')
    barbers = Barber.objects.all().order_by('barber_name')
    barber_reservations = []
    for barber in barbers:
        reservations = reservations_list.filter(barber=barber)
        num_of_reservations = reservations.__len__()
        item = {
            'barber': barber.barber_name,
            'num_of_reservations': num_of_reservations,
            'reservations': reservations
        }
        barber_reservations.append(item)
    total_reservations = 0
    for i in barber_reservations:
        total_reservations += i["num_of_reservations"]
    context = {
        'day': day,
        'barber_reservations': barber_reservations,
        'total_reservations': total_reservations
    }
    template = 'management/list_of_reservations.html'
    return render(request, template, context)
