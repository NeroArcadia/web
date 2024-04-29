from django.shortcuts import render , get_list_or_404
from .models import *
# Create your views here.

def page(request, page_id):
    page = get_list_or_404(page, id = page_id)
    return render(request, 'page.html', {'page':page})