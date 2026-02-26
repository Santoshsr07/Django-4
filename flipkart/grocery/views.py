from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def milk(request):
    return render(request, 'milk.html')

def dryfruit(request):
    return render(request, 'dryfruits.html')

def toys(request):
    return render(request, 'toys.html')

def bevrages(request):
    return render(request, 'bevrages.html')

