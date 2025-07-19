# boletas/views.py
from django.shortcuts import render

def index(request):
    boletas = [
        {"nombre": "Boleta Ciclo 2025-I", "archivo": "boleta_2025_1.pdf"},
        {"nombre": "Boleta Ciclo 2025-II", "archivo": "boleta_2025_2.pdf"},
    ]
    return render(request, "boletas/index.html", {"boletas": boletas})
