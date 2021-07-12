.PHONY: up
up: setup ## up docker containers
	docker-compose up -d

.PHONY: down
down: ## down(stop & remove) docker containers
	docker-compose down

.PHONY: stop
stop: ## stop docker containers
	docker-compose stop

.PHONY: setup
setup: network

network:
	@docker network create sample-dev > network

.PHONY: clean clean-postgres clean-network

clean: down clean-postgres clean-network

clean-network:
	docker network rm sample-dev
	rm network

clean-postgres:
	docker volume rm sample-django-githubaction_sample-data
