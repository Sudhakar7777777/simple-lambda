.PHONY: up down reboot help

## Run the service and watch for changes
up: 
	# docker-clean-images
	docker compose up -d

## Shut down the service and any associated volume
down:
	docker compose down --volumes

## Start from scratch again
reboot: down up

## Show logs from docker container
logs:
	docker logs -f localstack

docker-clean-images:
	docker image prune --force --filter "until=24h"

docker-clean-volumes:
	docker volume prune --force

docker-nuke:
	docker system prune --force --all

## Run a yarn command inside the container
%:
	docker-compose exec ern-processor yarn $@