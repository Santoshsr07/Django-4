from django.urls import path
from grocery import views

urlpatterns = [
    path('', views.milk),
    path('grocery/', views.dryfruit),
    path('Cars/', views.cars),
    path('bevrages/', views.bevrages),
    

]