.DEFAULT_GOAL := help
.PHONY: run help lint

run:
	docker-compose up --build

lint:
	flake8 .
