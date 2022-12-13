from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..decorators import paciente_required
from ..forms import PacienteSignUpForm
from ..models import Registro, User


@login_required
@paciente_required
def home_paciente(request):
    username_paciente = request.user.username
    id_paciente = User.objects.filter(username=username_paciente).values()[0]["id"]
    fichas = Registro.objects.filter(paciente_id=id_paciente)

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
