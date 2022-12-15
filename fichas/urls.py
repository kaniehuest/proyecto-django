from django.contrib import admin
from django.urls import include, path

from .views import views, medicos, pacientes, superuser

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),

    # Admin 
    path("superuser/", superuser.admin_panel, name="admin_panel"),
    path("superuser/eliminar/<int:id>", superuser.eliminar_medico, name="eliminar_medico"),
    path("superuser/info/<int:id>", superuser.info_medico, name="info_medico"),
    path("superuser/editar/username/<int:id>", superuser.editar_username_medico, name="editar_username_medico"),
    path("superuser/editar/nombres/<int:id>", superuser.editar_nombres_medico, name="editar_nombres_medico"),
    path("superuser/editar/apellidos/<int:id>", superuser.editar_apellidos_medico, name="editar_apellidos_medico"),
    path("superuser/editar/genero/<int:id>", superuser.editar_genero_medico, name="editar_genero_medico"),
    path("superuser/editar/telefono/<int:id>", superuser.editar_telefono_medico, name="editar_telefono_medico"),
    path("superuser/editar/email/<int:id>", superuser.editar_email_medico, name="editar_email_medico"),

    # Paciente
    path("pacientes/", pacientes.home_paciente, name="home_paciente"),
    path("pacientes/fichas/info/<int:id_ficha>/", pacientes.info_fichas, name="info_fichas_paciente"),

    # Medico
    path("medicos/", medicos.home, name="home_medico"),
    path("medicos/pacientes/eliminar/<int:id>/", medicos.eliminar_paciente, name="eliminar_paciente"),
    path("medicos/fichas/info/<int:id_ficha>/", medicos.info_fichas, name="info_fichas"),
    path("medicos/fichas/registrar/<int:id_paciente>/", medicos.crear_registro, name="registrar_ficha"),
    path("medicos/fichas/listar/<int:id_paciente>/", medicos.listar_fichas, name="listar_fichas"),
    path("medicos/fichas/confirmacion/", medicos.confirmar_registro, name="confirmacion"),
]