cnf ?= config.env
include $(cnf)
export $(shell sed 's/=.*//' $(cnf))

docker.:
	@echo 'building image for container'
	docker build -t $(APP_NAME) . 
docker-run: docker.
	@echo 'building and running'
	docker run -d --name="$(APP_NAME)"  -p 5000:5000 $(APP_NAME)
docker-shell: docker.
	@echo 'building and runnning with shell bash'
	docker run  -it --name="$(APP_NAME)" -p 5000:5000 $(APP_NAME) /bin/sh
shell:
	@echo 'running with shell only'
	docker run -it  --name="$(APP_NAME)" -p 5000:5000 $(APP_NAME) /bin/sh
docker-stop:
	@echo 'stopping $(APP_NAME)'
	docker stop $(APP_NAME)
	docker ps -a
