from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .forms import TreatmentForm
from .models import Treatment


def new_treatment(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            treatment = form.save()
            return HttpResponseRedirect('/')
    else:
        form = TreatmentForm(initial={'price': '0.00', 'duration': 'hh:mm:ss'})

    template = 'treatments/new_treatment.html'
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
    template = 'treatments/edit_treatment.html'
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
    template = 'treatments/edit_treatment.html'
    context = {
        'form': form,
        'treatments': treatments
    }
    return render(request, template, context)


def delete_treatment(request, treatment_id):
    treatment = get_object_or_404(Treatment, id=treatment_id)
    treatment.delete()
    return HttpResponseRedirect('/')