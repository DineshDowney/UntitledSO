from django.shortcuts import render, redirect

def homepage(request):
    return render(request, 'home/homepage.html')


def about_us(request):
    return render(request, 'home/About.html')
