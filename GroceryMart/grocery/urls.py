from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("shop/", views.shop, name="shop"),
    path("categories/", views.categories, name="categories"),
    path("offers/", views.offers, name="offers"),
    path("dairy/", views.dairy, name="dairy"),
    path("dryfruits/", views.dryfruits, name="dryfruits"),
    path("beverages/", views.beverages, name="beverages"),
    path("toys/", views.toys, name="toys"),
    # AUTH
    path("login/", views.login_view, name="login"),
    path("signup/", views.signup_view, name="signup"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    # CART
    path("cart/", views.cart, name="cart"),
]
