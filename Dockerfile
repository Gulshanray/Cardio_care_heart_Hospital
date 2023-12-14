FROM python:3
WORKDIR /django
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install djongo 
RUN pip install  pymongo
Run  python manage.py makemigrations
RUN python manage.py  migration

COPY . .
CMD python manage.py runserver 0.0.0.0:8000
