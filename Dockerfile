FROM python:3.8

EXPOSE 8000

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY /backend /app
COPY .env /app

RUN python3 manage.py collectstatic --noinput

CMD ["gunicorn", "config.wsgi", "--bind", "0.0.0.0:8000"]
