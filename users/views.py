from django.shortcuts import render, redirect
from django.http import HttpResponse
from users import forms
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
import random
# Create your views here.
User = get_user_model()


def register(request):
    if request.method == 'POST':
        RegForm = forms.Register(request.POST)
        if RegForm.is_valid():
            first_name = RegForm.cleaned_data.get("fname")
            last_name = RegForm.cleaned_data.get("lname")
            username = first_name+str(random.randint(1, 101))
            password = RegForm.cleaned_data.get("password1")
            email = RegForm.cleaned_data.get("email")
            auth_user = User.objects.create_user(username, email, password)
            auth_user.first_name = first_name
            auth_user.last_name = last_name
            auth_user.save()
            print(auth_user)
            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                messages.success(request, f"New account created: {username}")
                login(request, auth_user)
               # messages.info(request, f"You are logged in as: {username}")
                return redirect("../")
    RegForm = forms.Register()
    return render(request, 'register.html', {'form_dic': RegForm})


def user_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully")
    return render(request, "homepage.html")


def user_login(request):
    LogForm = forms.LoginForm(request.POST or None)
    print("User logged in: "+str(request.user.is_authenticated))
    if LogForm.is_valid():
        username = LogForm.cleaned_data.get("uname")
        password = LogForm.cleaned_data.get("password")
        auth_user = authenticate(username=username, password=password)
        if auth_user is not None:
            login(request, auth_user)
            messages.info(request, f"You are logged in as: {username}")
            return redirect("../")
    return render(request, 'login.html', {'form_dic': LogForm})
