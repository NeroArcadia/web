from django.shortcuts import render , get_list_or_404
from .models import *


def blog(request):
    post = Post.objects.all()
    return render(request, 'blog.html', {'post': post})

def category(request, category_id):
    category = get_list_or_404(Category,id = category_id)
    return render(request,'category.html', {'category': category})

#Category.objects.get