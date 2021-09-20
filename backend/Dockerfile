FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
    
RUN pip install --upgrade pip

RUN pip install -r /requirements.txt


RUN mkdir /backend
COPY ./backend /backend
WORKDIR /backend
# Run the application:
# CMD python manage.py runserver 0.0.0.0:8000