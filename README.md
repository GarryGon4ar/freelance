# freelance rest api 

## General info
This project is basic freelance rest api  , with developer and customer.

## REQUIREMENTS

This App Uses Python 3.6, Django 2.2.2, djangorestframework 3.9.4.

## INSTALLATION

To clone and run this repository, you'll need Git installed on your computer. I used virtualenv for this project, you may feel free to use the same. From your command line:

```
$ git clone https://github.com/GarryGon4ar/freelance.git
$ virtualenv sample_environment -p python3
$ source sample_environment/bin/activate
$ cd freelance
$ pip install -r requirements.txt
$ python manage.py runsever

## USAGE

to sign-up go to http://127.0.0.1:8000/api/users/
to sign-in go to http://127.0.0.1:8000/api/login/
to sign-out go to http://127.0.0.1:8000/api/logout/
to create a task go to http://127.0.0.1:8000/api/tasks/

if you are a developer go to detail page of your task http://127.0.0.1:8000/api/tasks/id , 
           where id is number representing id of task you want to perform, and use post method to perform.