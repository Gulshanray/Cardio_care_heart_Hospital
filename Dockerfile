# FROM python:3
# WORKDIR /django
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt
# RUN pip install djongo 
# RUN pip install  pymongo
# RUN  python manage.py makemigrations
# RUN python manage.py  migration

# COPY . .
# CMD python manage.py runserver 0.0.0.0:8000

# Use the official Python 3 image as a base image
FROM python:3

# Set the working directory inside the container
WORKDIR /django

# Copy the requirements file to the working directory
COPY requirements.txt requirements.txt

# Install the Python dependencies
RUN pip install -r requirements.txt

# Install Djongo and pymongo
RUN pip install djongo pymongo

# Copy the entire project to the working directory
COPY . .

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

