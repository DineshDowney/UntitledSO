from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("signup/", views.register),
    path("logout/", views.user_logout, name="timeout"),
    path("profile/", views.profile, name="UserProfile"),
    path("login/", views.user_login, name="timein"),
]
