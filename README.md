# Aspire Application
A project that implements a Python-based RESTful API application using the https://the-one-api.dev/ with at least the following endpoints
<img width="1440" alt="Screenshot 2022-06-04 at 21 45 19" src="https://user-images.githubusercontent.com/51092098/172024974-2260f864-4868-4002-9bcb-a4222b94e8b6.png">

## API Doc
* https://documenter.getpostman.com/view/11737108/TzJvfcrF

### How to Use and Test this Application
- Clone the Repository
- Create a .env file in the root directory and paste in the env variables
- Run `docker-compose up --build`
- run migrations `docker-compose exec web python manage.py makemigrations`
- run `docker-compose exec web python manage.py migrate`
- run tests `docker-compose exec web python manage.py test`
- Using the documentation available below, make api calls the endpoints provided.

## Technologies

* [Python 3.9](https://python.org) : Base programming language for development
* [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
* [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
* [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
* [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
* [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration
