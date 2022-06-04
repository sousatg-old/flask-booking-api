.DEFAULT_GOAL := help
.PHONY: run help lint

build:
	docker-compose build

run:
	docker-compose up --build

lint:
	flake8 .
