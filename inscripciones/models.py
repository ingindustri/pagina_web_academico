from django.db import models

class Inscripcion(models.Model):
    CARRERAS = [
        ('asistencia', 'Asistencia Administrativa'),
        ('electricidad', 'Electricidad Industrial'),
        ('contabilidad', 'Contabilidad'),
        ('construccion', 'Construcción Civil'),
        ('mecatronica', 'Mecatrónica Automotriz'),
        ('agropecuaria', 'Producción Agropecuaria'),
        ('mecanica', 'Mecánica de Producción Industrial'),
    ]

    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=8)
    correo = models.EmailField()
    carrera = models.CharField(max_length=50, choices=CARRERAS)
    fecha_registro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellidos}"

