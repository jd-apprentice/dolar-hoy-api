main: install
	make start

install:
	pip install -r requirements.txt

requirements:
	pip freeze > requirements.txt

dev:
	uvicorn main:app --reload --port 4500

start:
	uvicorn main:app --host 0.0.0.0 --port 4500

build:
	docker compose up -d --build

up:
	docker compose up -d