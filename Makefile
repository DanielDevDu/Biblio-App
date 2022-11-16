ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file ./backend/.env

endif

# Backend

develop-backend: ## Run backend in development mode
	@echo "Down backend"
	cd backend && docker-compose down
	@echo "Up backend"
	docker-compose up --build -d
	@echo "Show logs backend"
	docker-compose logs -f backend && cd ..

check-backend:
	@echo "Checking backend..."
	@cd backend && python manage.py check && cd ..

build-backend:
	@echo "Building backend..."
	cd backend && docker-compose up --build -d --remove-orphans && cd ..

up-backend:
	@echo "Starting backend..."
	cd backend && docker-compose up -d && cd ..

down-backend:
	@echo "Stopping backend..."
	cd backend && docker-compose down && cd ..

down-v-backend:
	@echo "Stopping backend and removing volumes..."
	cd backend && docker-compose down -v && cd ..

logs-backend:
	@echo "Showing backend logs..."
	cd backend && docker-compose logs && cd ..

c-logs-backend:
	@echo "Showing backend logs..."
	cd backend && docker-compose logs -f && cd ..

migrate:
	@echo "Migrating..."
	cd backend && docker-compose exec api python manage.py migrate && cd ..

makemigration:
	@echo "Making migration..."
	cd backend && docker-compose exec api python manage.py makemigrations && cd ..

createsuperuser:
	@echo "Creating superuser..."
	cd backend && docker-compose exec api python manage.py createsuperuser && cd ..

collectstatic:
	@echo "Collecting static files..."
	cd backend && docker-compose exec api python manage.py collectstatic --no-input && cd ..

volume:
	@echo "inspect volume..."
	cd backend && docker volume inspect backend_postgres_data_biblio && cd ..

backend:
	@echo "Inside of backend container..."
	cd backend && docker-compose exec -it api bash && cd ..

db:
	@echo "Inside of db container..."
	cd backend && docker-compose exec postgres-db-biblio psql --username=admin --dbname=biblio

# test:
# 	cd backend && docker-compose exec api pytest -p no:warnings --cov=.

# test-html:
# 	cd backend && docker-compose exec api pytest -p no:warnings --cov=. --cov-report=html

# flake8:
# 	cd backend && docker-compose exec api flake8 #

# black-check:
# 	cd backend && docker-compose exec api pip install --upgrade black==22.3.0
# 	cd backend && docker-compose exec api black --check --exclude=migrations .

# black-diff:
# 	cd backend && docker-compose exec api black --diff --exclude=migrations . #

# black:
# 	cd backend && docker-compose exec api black --exclude=migrations . #

# isort-check:
# 	cd backend && docker-compose exec api isort . --check-only --skip env --skip migrations #

# isort-diff:
# 	cd backend && docker-compose exec api isort . --diff --skip env --skip migrations #

# isort:
# 	cd backend && docker-compose exec api isort . --skip env --skip migrations #

# Frontent

build-frontend:
	@echo "Building frontend..."
	cd frontend && docker-compose up --build -d --remove-orphans && cd ..

up-frontend:
	@echo "Starting frontend..."
	cd frontend && docker-compose up -d && cd ..

down-frontend:
	@echo "Stopping frontend..."
	cd frontend && docker-compose down && cd ..

down-v-frontend:
	@echo "Stopping frontend and removing volumes..."
	cd frontend && docker-compose down -v && cd ..

logs-frontend:
	@echo "Showing frontend logs..."
	cd frontend && docker-compose logs && cd ..

c-logs-frontend:
	@echo "Showing frontend logs..."
	cd frontend && docker-compose logs -f && cd ..

frontend:
	@echo "Inside of frontend container..."
	cd frontend && docker-compose exec -it frontend-react bash && cd ..

# Shared or General

ports:
	@echo "Showing ports..."
	sudo lsof -i -P -n | grep LISTEN

composes:
	@echo "Showing docker-compose processes..."
	cd backend && docker-compose ps && cd ..
	cd frontend && docker-compose ps && cd ..

build:
	@echo "Building..."
	make build-backend
	make build-frontend

up:
	@echo "Starting..."
	make up-backend
	sleep 5 | echo "Waiting for backend to start"
	make up-frontend

down:
	@echo "Stopping..."
	make down-frontend
	make down-backend

down-v:
	@echo "Stopping and removing volumes..."
	make down-v-frontend
	make down-v-backend


