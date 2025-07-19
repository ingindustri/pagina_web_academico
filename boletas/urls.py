from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='boletas_index'),
]

# boletas/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'boletas/index.html')