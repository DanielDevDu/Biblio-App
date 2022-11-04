ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs

c-logs:
	docker-compose logs -f

migrate:
	docker-compose exec api python manage.py migrate

makemigration:
	docker-compose exec api python manage.py makemigrations

createsuperuser:
	docker-compose exec api python manage.py createsuperuser

collectstatic:
	docker-compose exec api python manage.py collectstatic --no-input #

down-v:
	docker-compose down -v

volume:
	docker volume inspect biblio_app_postgres_data

backend:
	docker-compose exec -it api bash

db:
	docker-compose exec postgres-db-biblio psql --username=admin --dbname=biblio

test:
	docker-compose exec api pytest -p no:warnings --cov=.

test-html:
	docker-compose exec api pytest -p no:warnings --cov=. --cov-report=html

flake8:
	docker-compose exec api flake8 #

black-check:
	docker-compose exec api pip install --upgrade black==22.3.0
	docker-compose exec api black --check --exclude=migrations .

black-diff:
	docker-compose exec api black --diff --exclude=migrations . #

black:
	docker-compose exec api black --exclude=migrations . #

isort-check:
	docker-compose exec api isort . --check-only --skip env --skip migrations #

isort-diff:
	docker-compose exec api isort . --diff --skip env --skip migrations #

isort:
	docker-compose exec api isort . --skip env --skip migrations #

ports:
	sudo lsof -i -P -n | grep LISTEN