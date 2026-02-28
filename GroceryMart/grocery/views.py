from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login

# ===== AUTH =====


def signup_view(request):
    form = UserCreationForm(request.POST or None)

    form.fields["username"].widget.attrs.update(
        {"placeholder": "Choose a username", "class": "form-input"}
    )

    form.fields["password1"].widget.attrs.update(
        {"placeholder": "Create password", "class": "form-input"}
    )

    form.fields["password2"].widget.attrs.update(
        {"placeholder": "Confirm password", "class": "form-input"}
    )

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("home")

    return render(request, "signup.html", {"form": form})


def login_view(request):
    form = AuthenticationForm(request, data=request.POST or None)

    form.fields["username"].widget.attrs.update(
        {"placeholder": "Email or Username", "class": "form-input"}
    )

    form.fields["password"].widget.attrs.update(
        {"placeholder": "Password", "class": "form-input"}
    )

    if form.is_valid():
        login(request, form.get_user())
        return redirect("home")

    return render(request, "login.html", {"form": form})


def cart(request):
    return render(request, "cart.html")


# Create your views here.
def home(request):
    return render(request, "home.html")


def shop(request):
    return render(request, "shop.html")


def offers(request):
    return render(request, "offers.html")


def dairy(request):
    return render(request, "dairy.html")


def dryfruits(request):
    return render(request, "dryfruits.html")


def toys(request):
    return render(request, "toys.html")


def beverages(request):
    return render(request, "beverages.html")


def categories(request):
    return render(request, "categories.html")
