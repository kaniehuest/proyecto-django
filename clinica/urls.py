from django.urls import include, path

from fichas.views import views, medicos, pacientes

urlpatterns = [
    path("", include("fichas.urls")),
    path("cuentas/", include("django.contrib.auth.urls")),
    path(
        "cuentas/registrar/paciente/",
        pacientes.PacienteSignUpView.as_view(),
        name="student_signup",
    ),
    path(
        "cuentas/registrar/medico/",
        medicos.MedicoSignUpView.as_view(),
        name="registrar_medico",
    ),
]
