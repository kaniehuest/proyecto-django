from django.contrib import admin
from django.urls import include, path

from .views import classroom, students, teachers

urlpatterns = [
    path('', classroom.home, name='home'),
    path('admin/', admin.site.urls),
    path('superuser/', teachers.admin_panel, name='admin_panel'),
    path('fichas/registrar/<int:id_paciente>/', teachers.crear_registro, name='registrar_ficha'),
    path('fichas/listar/<int:id>/', teachers.listar_fichas, name='listar_fichas'),
    path('fichas/info/<int:id_ficha>/', teachers.info_fichas, name='info_fichas'),

    path('students/', include(([
        path('', students.QuizListView.as_view(), name='quiz_list'),
        path('quiz/<int:pk>/', students.take_quiz, name='take_quiz'),
    ], 'classroom'), namespace='students')),

    path('teachers/', include(([
        path('', teachers.registro_home, name='quiz_change_list'),
    ], 'classroom'), namespace='teachers')),
]
