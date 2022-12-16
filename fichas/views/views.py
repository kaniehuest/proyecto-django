from django.shortcuts import redirect, render
from django.views.generic import TemplateView


class SignUpView(TemplateView):
    template_name = "registration/signup.html"


def home(request):
    if request.user.is_authenticated:
        if request.user.is_medico:
            return redirect("home_medico")
        elif request.user.is_superuser:
            return redirect("admin_panel")
        else:
            return redirect("home_paciente")
    return render(request, "home.html")
