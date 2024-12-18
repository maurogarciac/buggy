APP_NAME=buggy
TAG=0.0.1

.PHONY: test
test:
	docker compose up

.PHONY: start
start:
	uvicorn main:app --reload