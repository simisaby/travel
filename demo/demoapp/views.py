from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Team_members

# Create your views here.

def index(request):
    obj = Place.objects.all()
    team = Team_members.objects.all()
    return render(request, 'index.html', {'result': obj, 'teams':team})


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return HttpResponse("I am from contacts")

def details(request):
    return render(request,'details.html')

def thanks(request):
    return HttpResponse("Thanks")