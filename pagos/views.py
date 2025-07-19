from django.shortcuts import render

def index(request):
    return render(request, 'pagos/index.html')

def metodos_pago(request):
    return render(request, 'pagos/metodos.html')
