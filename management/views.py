from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TreatmentForm, BarberForm
from .models import Treatment, Barber
from checkout.models import Reservation
from datetime import date


def new_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            treatment = form.save()
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
        treatment_id = request.POST["treatment"]
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
    treatments = Treatment.objects.all()
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
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = TreatmentForm()
    treatments = Treatment.objects.all()
    template = 'management/edit_treatment.html'
    context = {
        'form': form,
        'treatments': treatments
    }
    return render(request, template, context)


def delete_treatment(request, treatment_id):
    treatment = get_object_or_404(Treatment, id=treatment_id)
    treatment.delete()
    return HttpResponseRedirect('/')

def new_barber(request):
    if request.method == 'POST':
        form = BarberForm(request.POST, request.FILES)
        if form.is_valid():
            barber = form.save()
            return HttpResponseRedirect('/')
    else:
        form = BarberForm(initial={'start_time': '08:00:00', 'end_time': '17:00:00'})

    template = 'management/new_barber.html'
    context = {
        'form': form
    }
    return render(request, template, context)


def get_barber(request):
    if request.method == 'POST':
        barber_id = request.POST["barber"]
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
    barbers = Barber.objects.all()
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
            return HttpResponseRedirect('/')
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
    return HttpResponseRedirect('/')


def list_of_reservations(request, day=date.today()):
    if request.method == 'POST':
        day = request.POST['day']
    reservations = Reservation.objects.filter(date=day).order_by('time')
    barbers = Barber.objects.all()
    context = {
        'reservations': reservations,
        'barbers': barbers,
        'day': day,
    }
    template = 'management/list_of_reservations.html'
    return render(request, template, context)
