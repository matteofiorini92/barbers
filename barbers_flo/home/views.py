from django.shortcuts import render


def home(request):
    """ A view to return the home page """
    return render(request, 'home/index.html')


def gallery(request):
    """ A view to return the gallery page """
    return render(request, 'home/gallery.html')


def team(request):
    """ A view to return the team page """
    return render(request, 'home/team.html')
