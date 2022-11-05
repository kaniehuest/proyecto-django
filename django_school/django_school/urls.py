from django.urls import include, path

from classroom.views import classroom, students, teachers

urlpatterns = [
    path('', include('classroom.urls')),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('cuentas/registrar/', classroom.SignUpView.as_view(), name='signup'),
    path('cuentas/registrar/paciente/', students.StudentSignUpView.as_view(), name='student_signup'),
    path('cuentas/registrar/medico/', teachers.TeacherSignUpView.as_view(), name='registrar_medico'),
]
