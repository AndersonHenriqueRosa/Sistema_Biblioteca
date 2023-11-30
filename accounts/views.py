from django.shortcuts import render, redirect
from django.contrib import auth, messages
from django.contrib.auth.models import User

# Create your views here.



def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        userVerify = auth.authenticate(request, email=email, password=password)
        print(userVerify)

        if userVerify == None:
            messages.info(request, "Email ou senha incorretos.")
            return redirect("login")
        else:
            auth.login(request, userVerify)
            return redirect("home")

    else:
        return render(request, "accounts/login.html")


def registration(request):
    if request.method == "POST":
        user = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        passwordConfirm = request.POST.get("passwordConfirm")

        User.objects.create_user(
            username=user, email=email, password=password
        )  # cliente
        # User.objects.create_superuser(username=user, email=email, password=password) #administrador
        return redirect("login")

    else:
        return render(request, "accounts/registration.html")


def logout(request):
    auth.logout(request)
    return redirect("login")