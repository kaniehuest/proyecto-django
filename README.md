# Proyecto Clínica con Django y Docker

## Setup manual

> You can have a step-by-step guide here: [Link](https://github.com/kaniehuest/proyecto-django/blob/master/manual-instalaci%C3%B3n/Manual%20de%20instalaci%C3%B3n%20en%20Windows%20de%20forma%20manual.pdf)

1. Configure `sample.env` and rename it to `.env`.
2. To run locally follow the instructions here: [Link](https://github.com/kaniehuest/proyecto-django/blob/master/clinica/settings.py#L92)
3. Run these commands:

```bash
$ pip install -r requirements.txt
$ python3 manage.py migrate
$ python3 manage.py createsuperuser
$ python3 manage.py runserver
```

## Setup with Docker

You can have a step-by-step guide here: [Link](https://github.com/kaniehuest/proyecto-django/blob/master/manual-instalaci%C3%B3n/Manual%20de%20instalaci%C3%B3n%20en%20Windows%20con%20Docker.pdf)

## User Manual

You can have instructions about the usage of the application here: [Link](https://github.com/kaniehuest/proyecto-django/blob/master/manual-usuario/Manual%20de%20usuario.pdf)