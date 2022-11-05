from django import forms

from classroom.models import Registro


class PostForm(forms.ModelForm):
    class Meta:
        model = Registro
        fields = ('medico', 'paciente', 'diagnostico',
                  'tratamiento', 'observaciones',
                  'examen_principal_bioquimico',
                  'examen_principal_orina',
                  'examen_principal_heces',
                  'examen_principal_glucosa',
                  'examen_resonancia_magnetica_torax',
                  'examen_resonancia_magnetica_columna',
                  'examen_resonancia_magnetica_cabeza',
                  'examen_resonancia_magnetica_abdomen',
                  'examen_ecografia_cabeza',
                  'examen_ecografia_torax',
                  'examen_ecografia_abdomen',
                  'examen_ecografia_brazo', 'tipo_consulta')