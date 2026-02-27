from django.urls import path
from grocery import views

urlpatterns = [
    path('', views.home, name="home"),
    path('shop/', views.shop, name="shop"),
    path('categories/', views.categories, name='categories'),
    path('offers/', views.offers, name='offers'),
    path('dairy/', views.dairy),
    path('toys/', views.toys),
    path('bevrages/', views.bevrages),
    path('dryfruits/', views.dryfruit), 
]