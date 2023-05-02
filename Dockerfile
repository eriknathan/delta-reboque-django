FROM python:3.9.16-slim-buster
LABEL authors="eriknathan"

COPY requirements.txt /

RUN pip install -r requirements.txt

COPY ./delta /delta/

COPY ./project /project/

COPY manage.py /

ENTRYPOINT python3 manage.py runserver