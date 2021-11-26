from django.shortcuts import render, redirect

# Create your views here.


def checkout(request):
    template = 'checkout/checkout.html'
    context = {
        'stripe_public_key': 'pk_test_51K00ZGB6ftyYlm0uHpm82edhLqQwxPLLszWXvpnkDsLpnl1PKVWJxjmqWw5srGRzdy1RqI2Wi4yCcFtNdx49QglP00XHmO35en',
        'client_secret': 'test_client_secret'
    }
    return render(request, template, context)