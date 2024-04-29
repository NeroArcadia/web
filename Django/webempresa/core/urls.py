from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio , name='inicio'),
    path('historia/', views.historia, name='historia'),
    path('base/',views.base, name='base'),
    path('visitanos/',views.visitanos, name='visitanos')
]
