from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from checkout.models import Reservation
from django.contrib.auth.models import User
from .forms import UserProfileForm, UserForm
from django.contrib import messages


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)
    user = get_object_or_404(User, username=request.user)
    # get 5 most recent reservations
    reservations = Reservation.objects.filter(user_profile=profile).order_by('-date')[:5]
    if request.method == 'POST':
        form_profile = UserProfileForm(request.POST, instance=profile)
        if form_profile.is_valid():
            form_profile.save()
        form_user = UserForm(request.POST, instance=user)
        if form_user.is_valid():
            form_user.save()
            messages.success(request, f'Details successfully updated for { user.username }')
        context = {
            'form_profile': form_profile,
            'form_user': form_user,
            'on_profile_page': True,
            'reservations': reservations,
        }
        return render(request, 'profiles/profile.html', context)
    else:
        form_profile = UserProfileForm(instance=profile)
        form_user = UserForm(instance=user)

    template = 'profiles/profile.html'
    context = {
        'form_profile': form_profile,
        'form_user': form_user,
        'on_profile_page': True,
        'reservations': reservations,
    }

    return render(request, template, context)
