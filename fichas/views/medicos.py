from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from ..decorators import medico_required, superuser_required
from ..forms import RegistroForm, MedicoSignUpForm
from ..models import User, Registro, Paciente


@login_required
@medico_required
def home(request):
    pacientes = User.objects.filter(is_paciente=1)
    if request.method == "GET":
        return render(request, "medicos/home.html", {"pacientes": pacientes})

    if request.method == "POST":
    # Obtiene el nombre desde el campo de input, si el nombre existe entonces devuelve el ID del usuario
    # y redirije a una página donde se listan todas sus fichas médicas
        try:
            nombre_paciente = request.POST.get("search")
            id_paciente = User.objects.filter(username=nombre_paciente).values()[0]["id"]
        except:
            return render(
                request,
                "medicos/home.html",
                {
                    "mensaje": "Error, el nombre no se encuentra registrado",
                    "pacientes": pacientes,
                },
            )

        if "crear_nuevo_registro" in request.POST:
            return redirect("registrar_ficha", id_paciente)

        elif "visualizar_registro" in request.POST:
            return redirect("listar_fichas", id_paciente)

    return render(request, "medicos/home.html", {"pacientes": pacientes})


@login_required
@medico_required
def crear_registro(request, id_paciente):
    ultimas_3_fichas = Registro.objects.filter(paciente_id=id_paciente)[:3]
    nombre_medico = request.user.username
    id_medico = User.objects.filter(username=nombre_medico).values()[0]["id"]
    nombre_paciente = User.objects.filter(id=id_paciente).values()[0]["username"]

    if request.method == "GET":
        data = {
            "nombre_medico": nombre_medico,
            "nombre_paciente": nombre_paciente,
            "ultimas_3_fichas": ultimas_3_fichas,
        }

        return render(request, "medicos/fichas_form.html", data)

    # Exámenes principales
    examen_principal_bioquimico = request.POST.get("examen_principal_bioquimico")
    examen_principal_orina = request.POST.get("examen_principal_orina")
    examen_principal_heces = request.POST.get("examen_principal_heces")
    examen_principal_glucosa = request.POST.get("examen_principal_glucosa")

    # Exámenes resonancia magnética
    examen_resonancia_magnetica_torax = request.POST.get(
        "examen_resonancia_magnetica_torax"
    )
    examen_resonancia_magnetica_columna = request.POST.get(
        "examen_resonancia_magnetica_columna"
    )
    examen_resonancia_magnetica_cabeza = request.POST.get(
        "examen_resonancia_magnetica_cabeza"
    )
    examen_resonancia_magnetica_abdomen = request.POST.get(
        "examen_resonancia_magnetica_abdomen"
    )

    # Exámenes ecografía
    examen_ecografia_cabeza = request.POST.get("examen_ecografia_cabeza")
    examen_ecografia_torax = request.POST.get("examen_ecografia_torax")
    examen_ecografia_abdomen = request.POST.get("examen_ecografia_abdomen")
    examen_ecografia_brazo = request.POST.get("examen_ecografia_brazo")

    diagnostico = request.POST.get("diagnostico")
    tratamiento = request.POST.get("tratamiento")
    observaciones = request.POST.get("observaciones")

    tipo_consulta = request.POST.get("tipo_consulta")

    data = {
        "paciente": id_paciente,
        "medico": id_medico,
        "examen_principal_bioquimico": examen_principal_bioquimico,
        "examen_principal_orina": examen_principal_orina,
        "examen_principal_heces": examen_principal_heces,
        "examen_principal_glucosa": examen_principal_glucosa,
        "examen_resonancia_magnetica_torax": examen_resonancia_magnetica_torax,
        "examen_resonancia_magnetica_columna": examen_resonancia_magnetica_columna,
        "examen_resonancia_magnetica_cabeza": examen_resonancia_magnetica_cabeza,
        "examen_resonancia_magnetica_abdomen": examen_resonancia_magnetica_abdomen,
        "examen_ecografia_cabeza": examen_ecografia_cabeza,
        "examen_ecografia_torax": examen_ecografia_torax,
        "examen_ecografia_abdomen": examen_ecografia_abdomen,
        "examen_ecografia_brazo": examen_ecografia_brazo,
        "diagnostico": diagnostico,
        "tratamiento": tratamiento,
        "observaciones": observaciones,
        "tipo_consulta": tipo_consulta,
    }

    request.session["ficha"] = data
    return redirect("confirmacion")


@login_required
@medico_required
def confirmar_registro(request):
    data = request.session["ficha"]

    if "confirmar_registro_ficha" in request.POST:
        ficha = RegistroForm(data)
        if ficha.is_valid():
            ficha = ficha.save()
            del request.session

        return redirect("home_medico")

    nombre_medico = request.user.username
    nombre_paciente = User.objects.filter(id=data["paciente"]).values()[0]["username"]

    return render(
        request,
        "medicos/confirmacion.html",
        {"ficha": data, "medico": nombre_medico, "paciente": nombre_paciente},
    )


@login_required
@medico_required
def info_fichas(request, id_ficha):
    template_name = "medicos/registro_info.html"
    registro = Registro.objects.get(id=id_ficha)
    identificador_paciente = registro.paciente_id

    ultimos_3_registros = Registro.objects.filter(paciente_id=identificador_paciente)[
        :3
    ]

    return render(
        request,
        template_name,
        {"registro": registro, "ultimos_3_registros": ultimos_3_registros},
    )


@login_required
@medico_required
def listar_fichas(request, id_paciente):
    fichas = Registro.objects.filter(paciente_id=id_paciente)
    return render(request, "medicos/listar_fichas.html", {"fichas": fichas})



@login_required
@medico_required
def eliminar_paciente(request, id):
    paciente = Paciente.objects.get(user_id=id)
    paciente.delete()
    paciente = User.objects.get(id=id)
    paciente.delete()
    return redirect("home_medico")

