from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..decorators import superuser_required
from ..forms import MedicoSignUpForm, User
from ..models import User

@login_required
@superuser_required
def admin_panel(request):
    medicos = User.objects.filter(is_medico=1)
    return render(request, "admin/admin_panel.html", {"medicos": medicos})

class MedicoSignUpView(CreateView):
    model = User
    form_class = MedicoSignUpForm
    template_name = "registration/signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "medico"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect("admin_panel")


@login_required
@superuser_required
def eliminar_medico(request, id):
    medico = User.objects.get(id=id)
    medico.delete()
    return redirect("admin_panel")

@login_required
@superuser_required
def info_medico(request, id):
    medico = User.objects.get(id=id)
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)

@login_required
@superuser_required
def editar_username_medico(request, id):
    username = request.POST.get("username")
    medico = User.objects.get(id=id)
    medico.username = username
    medico.save()
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)

@login_required
@superuser_required
def editar_nombres_medico(request, id):
    nombres = request.POST.get("nombres")
    medico = User.objects.get(id=id)
    medico.first_name = nombres
    medico.save()
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)

@login_required
@superuser_required
def editar_apellidos_medico(request, id):
    apellidos = request.POST.get("last_name")
    medico = User.objects.get(id=id)
    medico.last_name = apellidos
    medico.save()
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)

@login_required
@superuser_required
def editar_genero_medico(request, id):
    genero = request.POST.get("genero")
    medico = User.objects.get(id=id)
    medico.genero = genero
    medico.save()
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)

@login_required
@superuser_required
def editar_telefono_medico(request, id):
    telefono = request.POST.get("telefono")
    medico = User.objects.get(id=id)
    medico.telefono = telefono
    medico.save()
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)

@login_required
@superuser_required
def editar_email_medico(request, id):
    email = request.POST.get("email")
    medico = User.objects.get(id=id)
    medico.email = email
    medico.save()
    data = {"medico": medico}
    return render(request, "admin/info_medico.html", data)
