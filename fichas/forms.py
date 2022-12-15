from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from fichas.models import User, Registro, Paciente


class MedicoSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "genero", "telefono", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_medico = True
        if commit:
            user.save()
        return user


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = (
            "medico",
            "paciente",
            "diagnostico",
            "tratamiento",
            "observaciones",
            "examen_principal_bioquimico",
            "examen_principal_orina",
            "examen_principal_heces",
            "examen_principal_glucosa",
            "examen_resonancia_magnetica_torax",
            "examen_resonancia_magnetica_columna",
            "examen_resonancia_magnetica_cabeza",
            "examen_resonancia_magnetica_abdomen",
            "examen_ecografia_cabeza",
            "examen_ecografia_torax",
            "examen_ecografia_abdomen",
            "examen_ecografia_brazo",
            "tipo_consulta",
        )


class PacienteSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_paciente = True
        user.save()
        student = Paciente.objects.create(user=user)
        return user
