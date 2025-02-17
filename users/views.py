from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.db.models import Prefetch
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render


def login(request):

    context = {"title": "Home - Авторизация"}
    return render(request, "users/login.html", context)


def registration(request):

    context = {"title": "Home - Регистрация"}
    return render(request, "users/registration.html", context)


def profile(request):

    context = {
        "title": "Home - Кабинет",
    }
    return render(request, "users/profile.html", context)


def logout(request): ...
