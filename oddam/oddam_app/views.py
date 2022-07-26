from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse
from django.views import View


#
# def LandingPage(request):
#     answer = 'Landing page'
#     return HttpResponse(answer)

def landingpage(request):
    return render(request, 'index.html')


def addonation(request):
    return render(request, 'form.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')

# TEMPORARY, FOR TESTING
# def base(request):
#     return render(request, 'base.html')
