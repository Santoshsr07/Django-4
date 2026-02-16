from django.shortcuts import render


# Create your views here.
def milk(request):
    return render(request, 'milk.html')

def dryfruit(request):
    return render(request, 'dryfruit.html')

def cars(request):
    return render(request, 'cars.html')

def bevrages(request):
    return render(request, 'bevrages.html')

