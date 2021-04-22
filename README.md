# Aspire Application
A.

[![Aspire Application](https://github.com/Resa-Obamwonyi/aspire/workflows/Aspire/badge.svg)](https://github.com/Resa-Obamwonyi/aspire/actions)

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Description
A.

### How to Use and Test this Application
- Clone the Repository
- Run `docker-compose up --build`
- run migrations `docker-compose exec web python manage.py makemigrations`
- run `docker-compose exec web python manage.py migrate`
- run tests `docker-compose exec web python manage.py test`