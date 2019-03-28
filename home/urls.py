from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("about/",views.about_us,name="about"),
]