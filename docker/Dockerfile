FROM python:3.9

MAINTAINER Edward jimenez "edward.jimenez.m@gmail.com"

RUN apt-get update || : && apt-get install python -y
RUN apt-get install -y python-dev

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r pip-requirements.txt

#ENV PYTHONPATH "${PYTHONPATH}:./app"
#EXPOSE 8000

#ENTRYPOINT ["gunicorn", "registrations.wsgi"]
#ENTRYPOINT ["/app/scripts/entrypoint.sh"]
#ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]

