from django.shortcuts import render
from core.models import *

def servicios(request):
    project = Project.objects.all()
    return render(request, 'servicios.html', {'project':project})