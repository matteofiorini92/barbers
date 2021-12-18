from django.shortcuts import render


# https://docs.djangoproject.com/en/4.0/ref/views/#django.views.defaults.page_not_found

def page_not_found_view(request, exception):
    return render(request, '404.html', status=404)