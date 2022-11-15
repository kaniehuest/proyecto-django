from django.contrib import admin
from django.urls import include, path

from .views import views, medicos, pacientes

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("superuser/", medicos.admin_panel, name="admin_panel"),
    path(
        "pacientes/",
        include(
            (
                [
                    path("", pacientes.home_paciente, name="home"),
                    path(
                        "fichas/info/<int:id_ficha>/",
                        pacientes.info_fichas,
                        name="info_fichas_paciente",
                    ),
                ],
                "fichas",
            ),
            namespace="pacientes",
        ),
    ),
    path(
        "medicos/",
        include(
            (
                [
                    path("", medicos.home, name="home"),
                    path(
                        "fichas/info/<int:id_ficha>/",
                        medicos.info_fichas,
                        name="info_fichas",
                    ),
                    path(
                        "fichas/registrar/<int:id_paciente>/",
                        medicos.crear_registro,
                        name="registrar_ficha",
                    ),
                    path(
                        "fichas/listar/<int:id_paciente>/",
                        medicos.listar_fichas,
                        name="listar_fichas",
                    ),
                    path(
                        "fichas/confirmacion/",
                        medicos.confirmar_registro,
                        name="confirmacion",
                    ),
                ],
                "fichas",
            ),
            namespace="medicos",
        ),
    ),
]
