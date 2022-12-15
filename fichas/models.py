from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    GENEROS = [
        ("MASCULINO", 'masculino'),
        ("FEMENINO", 'femenino'),
    ]
    is_paciente = models.BooleanField(default=False, null=True)
    is_medico = models.BooleanField(default=False, null=True)
    telefono = models.CharField(blank=True, max_length=50, default="", null=True)
    genero = models.CharField(
        max_length=9,
        choices=GENEROS,
        default="MASCULINO",
        null=True
    )


class Paciente(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_DEFAULT, primary_key=True, default="")


# Registro
class Registro(models.Model):
    medico = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="", null=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_DEFAULT, default="", null=True)

    # Campos de texto
    diagnostico = models.TextField(blank=True, default="", null=True)
    tratamiento = models.TextField(blank=True, default="", null=True)
    observaciones = models.TextField(blank=True, default="", null=True)
    fecha_registro = models.DateTimeField(default=now, blank=True, null=True)

    # Tipo de cita medica
    tipo_consulta = models.CharField(default="Consulta médica", max_length=50, null=True)

    # Examenes
    examen_principal_bioquimico = models.BooleanField(default=False)
    examen_principal_orina = models.BooleanField(default=False)
    examen_principal_heces = models.BooleanField(default=False)
    examen_principal_glucosa = models.BooleanField(default=False)
    examen_resonancia_magnetica_torax = models.BooleanField(default=False)
    examen_resonancia_magnetica_columna = models.BooleanField(default=False)
    examen_resonancia_magnetica_cabeza = models.BooleanField(default=False)
    examen_resonancia_magnetica_abdomen = models.BooleanField(default=False)
    examen_ecografia_cabeza = models.BooleanField(default=False)
    examen_ecografia_torax = models.BooleanField(default=False)
    examen_ecografia_abdomen = models.BooleanField(default=False)
    examen_ecografia_brazo = models.BooleanField(default=False)
