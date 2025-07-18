# Generated by Django 5.2.4 on 2025-07-15 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('correo', models.EmailField(max_length=254)),
                ('carrera', models.CharField(choices=[('administracion', 'Asistencia Administrativa'), ('electricidad', 'Electricidad Industrial'), ('contabilidad', 'Contabilidad'), ('construccion', 'Construcción Civil'), ('mecatronica', 'Mecatrónica Automotriz'), ('agropecuaria', 'Producción Agropecuaria'), ('mecanica', 'Mecánica de Producción Industrial')], max_length=100)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
