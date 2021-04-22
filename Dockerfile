     # The first instruction is what image we want to base our container on
     FROM python:3.8

     # The environment variable ensures that the python output is set straight
     # to the terminal without buffering it first
     ENV PYTHONUNBUFFERED 1

     # create a root directory for our project in the container, mine is the name of my
     # Django project
     RUN mkdir /aspireProject

     # Set the working directory to your working directory
     WORKDIR /aspireProject

     # Copy the current directory contents into the container at your working directory
     ADD . /aspireProject/

     # Install any needed packages specified in requirements.txt (this would be created)
     RUN pip install -r requirements.txt
