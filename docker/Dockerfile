FROM python:3.9.2

MAINTAINER Edward jimenez "edward.jimenez.m@gmail.com"

RUN apt-get update || : && apt-get install python -y
RUN apt-get install -y python-dev

RUN mkdir /app
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN pip install -r pip-requirements.txt

#RUN python manage.py migrate
#ENV PYTHONPATH "${PYTHONPATH}:./app"
EXPOSE 8000

#ENTRYPOINT ["gunicorn", "--config", "gunicorn_config.py", "wsgi:application"]
#ENTRYPOINT ["/app/scripts/entrypoint.sh"]
ENTRYPOINT ["python", "manage.py", "runserver"]

