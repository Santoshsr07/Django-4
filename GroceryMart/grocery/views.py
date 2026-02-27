from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def shop(request):
    return render(request, 'shop.html')

def offers(request):
    return render(request, 'offers.html')

def dairy(request):
    return render(request, 'dairy.html')

def dryfruit(request):
    return render(request, 'dryfruits.html')

def toys(request):
    return render(request, 'toys.html')

def bevrages(request):
    return render(request, 'bevrages.html')

def categories(request):
    return render(request, 'categories.html')