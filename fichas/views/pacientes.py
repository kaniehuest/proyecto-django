from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView
from django.http import HttpResponse

from ..decorators import paciente_required
from ..forms import PacienteSignUpForm
from ..models import Registro, User, Paciente


@login_required
@paciente_required
def home_paciente(request):
    id = request.user.id
    fichas = Registro.objects.filter(paciente_id=id)

    return render(request, "pacientes/home_paciente.html", {"fichas": fichas})


@login_required
@paciente_required
def info_fichas(request, id_ficha):
    registro = Registro.objects.get(id=id_ficha)
    identificador_paciente = registro.paciente_id

    ultimos_3_registros = Registro.objects.filter(paciente_id=identificador_paciente)[
        :3
    ]

    return render(
        request,
        "pacientes/info_ficha.html",
        {"registro": registro, "ultimos_3_registros": ultimos_3_registros},
    )


class PacienteSignUpView(CreateView):
    model = User
    form_class = PacienteSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "student"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect("home_medico")

@login_required
@paciente_required
def info_paciente(request):
    paciente_id = request.user.id
    paciente = User.objects.get(id=paciente_id)
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def editar_username_paciente(request, id):
    username = request.POST.get("username")
    paciente = User.objects.get(id=id)
    paciente.username = username
    paciente.save()
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def editar_nombres_paciente(request, id):
    nombres = request.POST.get("nombres")
    paciente = User.objects.get(id=id)
    paciente.first_name = nombres
    paciente.save()
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def editar_apellidos_paciente(request, id):
    apellidos = request.POST.get("last_name")
    paciente = User.objects.get(id=id)
    paciente.last_name = apellidos
    paciente.save()
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def editar_genero_paciente(request, id):
    genero = request.POST.get("genero")
    paciente = User.objects.get(id=id)
    paciente.genero = genero
    paciente.save()
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def editar_telefono_paciente(request, id):
    telefono = request.POST.get("telefono")
    paciente = User.objects.get(id=id)
    paciente.telefono = telefono
    paciente.save()
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def editar_email_paciente(request, id):
    email = request.POST.get("email")
    paciente = User.objects.get(id=id)
    paciente.email = email
    paciente.save()
    data = {"paciente": paciente}
    return render(request, "pacientes/info_paciente.html", data)

@login_required
@paciente_required
def eliminar_paciente(request, id):
    paciente = Paciente.objects.get(user_id=id)
    paciente.delete()
    paciente = User.objects.get(id=id)
    paciente.delete()
    return redirect("home")
