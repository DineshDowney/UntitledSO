from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("signup/", views.register),
    path("about/",views.about_us,name="about"),
    path("logout/", views.user_logout, name="timeout"),
    path("login/", views.user_login, name="timein"),
]