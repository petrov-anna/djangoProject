FROM openjdk:20
FROM python:latest

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "django-admin", "runserver", "0.0.0.0:8000"]