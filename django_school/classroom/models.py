from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.timezone import now


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)




# # Paciente
# class Paciente(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
#     registros = models.ManyToManyField(Registro, through='TakenQuiz')

#     def get_unanswered_questions(self, quiz):
#         answered_questions = self.quiz_answers \
#             .filter(answer__question__quiz=quiz) \
#             .values_list('answer__question__pk', flat=True)
#         questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
#         return questions

#     def __str__(self):
#         return self.user.username


class Paciente(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.user.username


# Registro
class Registro(models.Model):
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    # Campos de texto
    diagnostico = models.TextField(blank=True)
    tratamiento = models.TextField(blank=True)
    observaciones = models.TextField(blank=True)
    fecha_registro = models.DateTimeField(default=now, blank=True)

    # Tipo de cita medica
    tipo_consulta = models.CharField(default="Consulta Medica", max_length=50)

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
