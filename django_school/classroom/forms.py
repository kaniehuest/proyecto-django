from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from classroom.models import (Answer, Question, Student, StudentAnswer,
                              Subject, User, Registro)


class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user

class RegistroForm(forms.ModelForm):
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



class StudentSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user


# class StudentInterestsForm(forms.ModelForm):
#     class Meta:
#         model = Student
#         fields = ('interests', )
#         widgets = {
#             'interests': forms.CheckboxSelectMultiple
#         }



