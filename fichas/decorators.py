from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test


def paciente_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    """
    Decorator para las vistas que requieren que el usuario sea un paciente,
    redirige a la página de log-in si es necesario
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_paciente,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def medico_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    """
    Decorator para las vistas que requieren que el usuario sea un médico,
    redirige a la página de log-in si es necesario
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_medico,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator


def superuser_required(
    function=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url="login"
):
    """
    Decorator for views that checks that the logged in user is an admin,
    redirects to the log-in page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
