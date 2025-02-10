from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'QLHS/cart.html')
def checkout(request):
    return render(request, 'QLHS/checkout.html')