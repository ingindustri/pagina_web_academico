from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inscripciones'),
    path('descargar_excel/', views.descargar_excel, name='descargar_excel'),
]
