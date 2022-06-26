.DEFAULT_GOAL := help
.PHONY: dev build run help lint update-swagger

dev:
	docker-compose -f docker-compose.dev.yml up --build

build:
	docker-compose build

run:
	docker-compose up --build

lint:
	flake8 .

update-swagger:
	python3 tools/update.py --ui --editor
