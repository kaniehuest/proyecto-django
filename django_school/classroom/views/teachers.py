from ast import Try
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models import Avg, Count
from django.forms import inlineformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from ..decorators import teacher_required, superuser_required
from ..forms import BaseAnswerInlineFormSet, QuestionForm, TeacherSignUpForm, RegistroForm
from ..models import Answer, Question, Quiz, User, Registro, Student


class TeacherSignUpView(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        #login(self.request, user)
        return redirect('admin_panel')


@login_required
@teacher_required
def registro_home(request):
    template_name = 'classroom/teachers/registro_home.html'

    if request.method == 'GET':
        return render(request, template_name)

    # Obtiene el nombre desde el campo de input, si el nombre existe entonces devuelve el ID del usuario
    # y redirije a una página donde se listan todas sus fichas médicas
    try:
        nombre_paciente = request.POST.get('search')
        id_paciente = User.objects.filter(
            username=nombre_paciente).values()[0]['id']
    except:
        return render(request, template_name, {'mensaje': 'Error, el nombre no se encuentra registrado'})

    if 'crear_nuevo_registro' in request.POST:
        return redirect('registrar_ficha', id_paciente)

    elif 'visualizar_registro' in request.POST:
        return redirect('listar_fichas', id_paciente)

    return render(request, template_name)


@login_required
@teacher_required
def crear_registro(request, id_paciente):
    if request.method == 'GET':
        username_medico = request.user.username
        id_medico = User.objects.filter(
            username=username_medico).values()[0]['id']
        ultimas_3_fichas = Registro.objects.filter(paciente_id=id_paciente)[:3]
        username_paciente = User.objects.filter(
            id=id_paciente).values()[0]['username']
        data = {'medico': username_medico,
                'id_medico': id_medico ,
                'paciente': username_paciente,
                'id_paciente': id_paciente,
                'ultimas_3_fichas': ultimas_3_fichas}

        return render(request, 'classroom/teachers/registro_form.html', data)
    
    id_paciente= request.POST.get('id_paciente')
    nombre_paciente= request.POST.get('paciente')

    id_medico = request.POST.get('id_medico')
    nombre_medico = request.POST.get('medico')

    # Exámenes principales
    examen_principal_bioquimico= request.POST.get('examen_principal_bioquimico')
    examen_principal_orina = request.POST.get('examen_principal_orina')
    examen_principal_heces = request.POST.get('examen_principal_heces')
    examen_principal_glucosa = request.POST.get('examen_principal_glucosa')

    # Exámenes resonancia magnética
    examen_resonancia_magnetica_torax = request.POST.get('examen_resonancia_magnetica_torax')
    examen_resonancia_magnetica_columna = request.POST.get('examen_resonancia_magnetica_columna')
    examen_resonancia_magnetica_cabeza = request.POST.get('examen_resonancia_magnetica_cabeza')
    examen_resonancia_magnetica_abdomen = request.POST.get('examen_resonancia_magnetica_abdomen')

    # Exámenes ecografía
    examen_ecografia_cabeza = request.POST.get('examen_ecografia_cabeza')
    examen_ecografia_torax = request.POST.get('examen_ecografia_torax')
    examen_ecografia_abdomen = request.POST.get('examen_ecografia_abdomen')
    examen_ecografia_brazo = request.POST.get('examen_ecografia_brazo')

    diagnostico = request.POST.get('diagnostico')
    tratamiento = request.POST.get('tratamiento')
    observaciones = request.POST.get('observaciones')
    
    tipo_consulta = request.POST.get('tipo_consulta')

    data = {"id_paciente"}

    return render(request, 'classroom/teachers/confirmation.html')
    



@login_required
@teacher_required
def info_fichas(request, id_ficha):
    template_name = 'classroom/teachers/registro_info.html'
    registro = Registro.objects.get(id=id_ficha)
    identificador_paciente = registro.paciente_id

    ultimos_3_registros = Registro.objects.filter(
        paciente_id=identificador_paciente)[:3]

    return render(request, template_name, {'registro': registro, 'ultimos_3_registros': ultimos_3_registros})


@login_required
@superuser_required
def admin_panel(request):
    return render(request, 'classroom/teachers/admin_panel.html')


def listar_fichas(request, id):
    fichas = Registro.objects.filter(paciente_id=id)
    return render(request, 'classroom/teachers/listar_fichas.html', {'fichas': fichas})
