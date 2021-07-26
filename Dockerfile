FROM python:3.8-slim-buster

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SECRET_KEY fake

#Install apache
RUN apt update -y
RUN apt install apache2 apache2-dev -y

#Install python deps
RUN pip install --upgrade pip 
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

#Copy app
COPY . /app/

#Generate static files
RUN python manage.py collectstatic

#Announce we use port 8000
EXPOSE 8000

#Expose the database
VOLUME  /app/database

#Ruuunnnnnnn !!!!!!!!!!!
CMD ["python", "manage.py", "runmodwsgi", "--user=www-data", "--group=www-data", "--port=8000"]
