from django.db import models

class ComprobantePago(models.Model):
    estudiante = models.CharField(max_length=100)
    archivo = models.FileField(upload_to='comprobantes/')
    fecha_subida = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago de {self.estudiante}"
