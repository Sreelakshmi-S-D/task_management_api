# Task Management API
This project is a simple Task Management REST API built using **Django** and **Django REST Framework** as part of a technical assignment.

## Python Version
Python 3.10+

## Setup Instructions
Create a virtual environment:
python -m venv venv 

Activate the virtual environment:

windows:
venv\Scripts\activate
macOS / Linux:
source venv/bin/activate

cd task_app

## Migrations
python manage.py makemigrations
python manage.py migrate

## Server run command
python manage.py runserver

## Test execution command
python manage.py test

## Sample API request
POST /api/tasks/
{
  "title": "My Task",
  "status": "Pending"
}

GET /api/tasks/