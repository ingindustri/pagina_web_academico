from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='pagos_index'),
    path('metodos/', views.metodos_pago, name='metodos_pago'),
]
