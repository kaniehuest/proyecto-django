from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "registration/signup.html"


def home(request):
    if request.user.is_authenticated:
        if request.user.is_medico:
            return redirect("medicos:home")
        elif request.user.is_superuser:
            return redirect("admin_panel")
        else:
            return redirect("pacientes:home")
    return render(request, "home.html")
