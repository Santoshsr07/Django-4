from django.urls import path
from grocery import views

urlpatterns = [
    path('', views.home),
    path('milk/', views.milk),
    path('toys/', views.toys),
    path('bevrages/', views.bevrages),
    path('dryfruits',views.dryfruit),
    

]