from django.contrib import admin
from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),
    path('admin/', admin.site.urls),
    path('superuser/', teachers.admin_panel, name='admin_panel'),
    path('fichas/registrar/<int:id_paciente>/', teachers.crear_registro, name='registrar_ficha'),
    path('fichas/listar/<int:id>/', teachers.listar_fichas, name='listar_fichas'),
    path('fichas/confirmacion/', teachers.confirmar_registro, name='confirmacion'),

    path('pacientes/', include(([
        path('', students.home_paciente, name='quiz_list'),
        path('fichas/info/<int:id_ficha>/', students.info_fichas, name='info_fichas_paciente'),
    ], 'classroom'), namespace='pacientes')),

    path('medicos/', include(([
        path('', teachers.registro_home, name='quiz_change_list'),
        path('fichas/info/<int:id_ficha>/', teachers.info_fichas, name='info_fichas'),
    ], 'classroom'), namespace='medicos')),
]
