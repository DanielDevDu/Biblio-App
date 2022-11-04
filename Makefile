ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file ./backend/.env

endif

# Backend

build-backend:
	cd backend && docker-compose up --build -d --remove-orphans && cd ..

up-backend:
	cd backend && docker-compose up -d && cd ..

down-backend:
	cd backend && docker-compose down && cd ..

down-v-backend:
	cd backend && docker-compose down -v && cd ..

logs-backend:
	cd backend && docker-compose logs && cd ..

c-logs-backend:
	cd backend && docker-compose logs -f && cd ..

migrate:
	cd backend && docker-compose exec api python manage.py migrate && cd ..

makemigration:
	cd backend && docker-compose exec api python manage.py makemigrations && cd ..

createsuperuser:
	cd backend && docker-compose exec api python manage.py createsuperuser && cd ..

collectstatic:
	cd backend && docker-compose exec api python manage.py collectstatic --no-input && cd ..

volume:
	docker volume inspect biblio_app_postgres_data

backend:
	docker-compose exec -it api bash

db:
	cd backend && docker-compose exec postgres-db-biblio psql --username=admin --dbname=biblio

test:
	cd backend && docker-compose exec api pytest -p no:warnings --cov=.

test-html:
	cd backend && docker-compose exec api pytest -p no:warnings --cov=. --cov-report=html

flake8:
	cd backend && docker-compose exec api flake8 #

black-check:
	cd backend && docker-compose exec api pip install --upgrade black==22.3.0
	cd backend && docker-compose exec api black --check --exclude=migrations .

black-diff:
	cd backend && docker-compose exec api black --diff --exclude=migrations . #

black:
	cd backend && docker-compose exec api black --exclude=migrations . #

isort-check:
	cd backend && docker-compose exec api isort . --check-only --skip env --skip migrations #

isort-diff:
	cd backend && docker-compose exec api isort . --diff --skip env --skip migrations #

isort:
	cd backend && docker-compose exec api isort . --skip env --skip migrations #

# Frontent

build-frontend:
	cd frontend && docker-compose up --build -d --remove-orphans && cd ..

up-frontend:
	cd frontend && docker-compose up -d && cd ..

down-frontend:
	cd frontend && docker-compose down && cd ..

down-v-frontend:
	cd frontend && docker-compose down -v && cd ..

logs-frontend:
	cd frontend && docker-compose logs && cd ..

c-logs-frontend:
	cd frontend && docker-compose logs -f && cd ..

# Shared or General

ports:
	sudo lsof -i -P -n | grep LISTEN