from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe
from django.utils.timezone import now



class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Subject(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=7, default='#007bff')

    def __str__(self):
        return self.name

    def get_html_badge(self):
        name = escape(self.name)
        color = escape(self.color)
        html = '<span class="badge badge-primary" style="background-color: %s">%s</span>' % (color, name)
        return mark_safe(html)


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='quizzes')
    fecha_registro = models.DateTimeField(default=now, blank=True)

    def __str__(self):
        return self.name


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

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.CharField('Question', max_length=255)

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    quizzes = models.ManyToManyField(Quiz, through='TakenQuiz')
    interests = models.ManyToManyField(Subject, related_name='interested_students')

    def get_unanswered_questions(self, quiz):
        answered_questions = self.quiz_answers \
            .filter(answer__question__quiz=quiz) \
            .values_list('answer__question__pk', flat=True)
        questions = quiz.questions.exclude(pk__in=answered_questions).order_by('text')
        return questions

    def __str__(self):
        return self.user.username


class TakenQuiz(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='taken_quizzes')
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='taken_quizzes')
    score = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)


class StudentAnswer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, related_name='+')


# Registro
class Registro(models.Model):
    medico = models.ForeignKey(User, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Student, on_delete=models.CASCADE)
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

