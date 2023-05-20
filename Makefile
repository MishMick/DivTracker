build-local:
	DOCKER_BUILDKIT=1 docker-compose -f docker-compose.yml build

local:
	docker-compose -f docker-compose.yml up