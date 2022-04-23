FROM python:3.10-slim-buster

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r --no-cache-dir requirements.txt

COPY /backend /app
COPY .env /app

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
