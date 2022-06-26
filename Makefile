.DEFAULT_GOAL := help
.PHONY: run help lint

build:
	docker-compose build

run:
	docker-compose up --build

lint:
	flake8 .

update-swagger:
	python3 tools/update.py --ui --editor
