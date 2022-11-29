FROM python:alpine3.16

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apk update \
	&& apk add gcc musl-dev mariadb-connector-c-dev \
	&& pip install --upgrade pip

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python","manage.py", "runserver", "0.0.0.0:8000"]