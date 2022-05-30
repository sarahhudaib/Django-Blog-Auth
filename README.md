# Django Permissions & Postgresql
Author: Sarah Hudaib

# Challenge
- Add JWT Authentication to your API.
Install needed libraries in project configuration and/or site settings.

- Keep any pre-existing authentication so DRF Browsable API still usable.
Install needed libraries in project configuration and/or site settings.

# Architecture
- Python 3.9.5 
- Django 4.0.4
- Docker 20.10.12
- Django REST Framework 3.13.1
- Docker Compose 1.25.0-1
- Django REST Framework-SimpleJWT 5.2.0


# Try it out by installing the requirements. (Works only with python >= 3.8, due to Django 4)
```
# Djang
$ pip install django
pip install django_rest_framework

# env
$ python -m venv django_env
$ source ./django_env/bin/activate

# requirements
$ poetry export -f requirements.txt --output requirements.txt

```
install docker
```
sudo apt-get update
sudo apt-get upgrade
sudo apt install docker.io
systemctl start docker
systemctl enable docker
docker --version
```

# Run the Project
Open Console in Main Project Directory.

```
$ git clone git@github.com:sarahhudaib/Django-Blog-App.git
$ cd Django-Blog-App
$ python manage.py runserver
on your browser http://127.0.0.1:8000
```




