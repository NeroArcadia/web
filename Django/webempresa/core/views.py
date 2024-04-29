from django.shortcuts import render
from Services.models import * 


def inicio(request):
    
    return render(request, 'inicio.html')

def historia(request):
    return render(request, 'historia.html')


def visitanos(request):
    return render(request, 'visitanos.html')


def base(request):
    return render(request, 'base.html')
