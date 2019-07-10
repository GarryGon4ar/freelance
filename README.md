# freelance rest api 

## General info
This project is basic freelance app built with REST API, with developer and customer. A customer can create a task, and developer then perform it and get money on his balance. 


## REQUIREMENTS

This App Uses Python 3.6, Django 2.2.2, djangorestframework 3.9.4, django-allauth 0.39.1, django-rest-auth 0.9.5, see all the requirements in requirements.txt.

## INSTALLATION

To clone and run this repository, you'll need Git installed on your computer. I used virtualenv for this project, you may feel free to use the same. From your command line:

```
$ git clone https://github.com/GarryGon4ar/freelance.git
$ virtualenv sample_environment -p python3
$ source sample_environment/bin/activate
$ cd freelance
$ pip install -r requirements.txt
$ python manage.py runsever

$ python manage.py makemigrations
$ python manage.py migrate

## USAGE

to sign-up go to http://127.0.0.1:8000/users/
to sign-in go to http://127.0.0.1:8000/rest-auth/login/
to sign-out go to http://127.0.0.1:8000/rest-auth/logout/
to create a task go to http://127.0.0.1:8000/tasks/
if you are a developer go to detail page of your task http://127.0.0.1:8000/task/id ,where id is number representing id of task you want to perform
or on the tasks page , click by url of task that you want to perform 
          and use patch method to perform it.