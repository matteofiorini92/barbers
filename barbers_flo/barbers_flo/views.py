from django.shortcuts import render


def home(request):
    """ A view to return the home page """
    return render(request, 'barbers_flo/home.html')
