compose-up:
	sudo docker-compose up

compose-up-detached:
	sudo docker-compose up -d

postgres-shell:
	sudo docker-compose exec db psql -h 127.0.0.1 -U app -d movies_database

django-migrate:
	sudo docker-compose exec backend python3 manage.py migrate

django-collectstatic:
	sudo docker-compose exec backend python3 manage.py collectstatic --noinput

django-createsuperuser:
	sudo docker-compose exec backend python3 maange.py createsuperuser
