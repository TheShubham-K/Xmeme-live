build:
	docker build --force-rm $(options) -t  xmeme:latest .

build-prod:
	$(MAKE) build options="--target production"

compose-start:
	docker-compose up --remove-orphans &(options)

compose-stop:
	docker-compose down --remove-orphans &(options)
