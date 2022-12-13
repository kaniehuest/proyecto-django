from django.contrib import admin
from django.urls import include, path

from .views import views, medicos, pacientes

urlpatterns = [
    path("", views.home, name="home"),
    path("admin/", admin.site.urls),
    path("superuser/", medicos.admin_panel, name="admin_panel"),
    path("superuser/eliminar/<int:id>", medicos.eliminar_medico, name="eliminar_medico"),
    path("pacientes/", pacientes.home_paciente, name="home_paciente"),
    path("pacientes/fichas/info/<int:id_ficha>/", pacientes.info_fichas, name="info_fichas_paciente"),
    path("medicos/", medicos.home, name="home_medico"),
    path("medicos/pacientes/eliminar/<int:id>/", medicos.eliminar_paciente, name="eliminar_paciente"),
    path("medicos/fichas/info/<int:id_ficha>/", medicos.info_fichas, name="info_fichas"),
    path("medicos/fichas/registrar/<int:id_paciente>/", medicos.crear_registro, name="registrar_ficha"),
    path("medicos/fichas/listar/<int:id_paciente>/", medicos.listar_fichas, name="listar_fichas"),
    path("medicos/fichas/confirmacion/", medicos.confirmar_registro, name="confirmacion"),
]