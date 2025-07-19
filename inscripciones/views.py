from django.shortcuts import render, redirect
from django.http import FileResponse
from .forms import InscripcionForm
import openpyxl
import os
from django.conf import settings

def index(request):
    if request.method == 'POST':
        form = InscripcionForm(request.POST)
        if form.is_valid():
            inscripcion = form.save()

            # Ruta del archivo Excel
            excel_path = os.path.join(settings.BASE_DIR, 'inscripciones.xlsx')

            # Crear si no existe
            if not os.path.exists(excel_path):
                wb = openpyxl.Workbook()
                ws = wb.active
                ws.title = "Inscripciones"
                ws.append(['Nombre', 'Apellidos', 'DNI', 'Correo', 'Carrera', 'Fecha de Registro'])
            else:
                wb = openpyxl.load_workbook(excel_path)
                ws = wb.active

            # Agregar datos (versión sin choices)
            ws.append([
                inscripcion.nombre,
                inscripcion.apellidos,
                inscripcion.dni,
                inscripcion.correo,
                inscripcion.carrera,
                inscripcion.fecha_registro.strftime('%Y-%m-%d %H:%M')
            ])

            wb.save(excel_path)
            return render(request, 'inscripciones/exito.html')
    else:
        form = InscripcionForm()

    return render(request, 'inscripciones/index.html', {'form': form})

def descargar_excel(request):
    file_path = os.path.join(settings.BASE_DIR, 'inscripciones.xlsx')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='inscripciones.xlsx')
    else:
        return render(request, 'inscripciones/no_excel.html')
