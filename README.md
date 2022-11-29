# proyecto-django

## Setup

-  Local:

> To run locally you have to change the default DATABASE on '/clinica/settings.py:DATABASES' to sqlite3.

```sh
$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python3 manage.py runserver
```

-  Docker compose:

```sh
docker-compose up -d
```

## First time commands

-  To make migrations:

```sh
python3 manage.py migrate
```

-  To create django superuser:

```sh
python3 manage.py createsuperuser
```

> If you setup the project on docker, run the commands inside the django container with `docker exec -it django /bin/sh`
