from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='informes_index'),
]
