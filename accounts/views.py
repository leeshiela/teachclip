from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from accounts.forms import SignUpForm, LoginForm

def create_teacher_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_confirmation = form.cleaned_data["password_confirmation"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]

            if password == password_confirmation:
                user = User.objects.create_user(
                    username,
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                )

                login(request, user)
                return redirect("teacher_home")
            else:
                form.add_error("password", "Passwords do not match")
    else:
        form = SignUpForm()
    context = {
        "signupform": form,
    }
    return render(request, "accounts/teacher_signup.html", context)


def teacher_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                request,
                username=username,
                password=password,
            )
            if user is not None:
                login(request,user)
                return redirect("teacher_home")
    else:
        form = LoginForm()
    context = {
        "loginform": form,
    }
    return render(request, "accounts/teacher_login.html", context)

def user_logout(request):
    logout(request)
    return redirect("info")
