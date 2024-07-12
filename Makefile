#
# Tryffle
#

#
# BOOTSTRAP:
# 	make bootstrap
# then follow instructions
#

MAKEFLAGS+="-j 2"

bootstrap:
	@[ ! -f .env ] && cp env.tpl .env || echo ".env file already exist ! keep it intact !"
	@echo "Please edit ./.env"
	@echo "Set adhoc STAGE target between 'local,staging,prod'. It will use the related compose file."
	@echo "Run 'make info' to check."
	@echo "IMPORTANT: For staging/production change postgres password to use a more complicated one."
	@echo "IMPORTANT: For production, postgres will be the "app common" postgres server to save ressources and backup maintenance."
	@echo "To init Django, make up + make init"

info:
	@export $(sed 's/#.*//g' .env | xargs) > /dev/null
	@echo "stage: ${STAGE}"

build:
	@export $(sed 's/#.*//g' .env | xargs) > /dev/null
	@cd tryffle && docker compose -f docker-compose.${STAGE}.yml build

config:
	@export $(sed 's/#.*//g' .env | xargs) > /dev/null
	@cd tryffle && docker compose -f docker-compose.${STAGE}.yml config

up:
	@export $(sed 's/#.*//g' .env | xargs) > /dev/null
	@cd tryffle && docker compose -f docker-compose.${STAGE}.yml up -d

down:
	@export $(sed 's/#.*//g' .env | xargs) > /dev/null
	@cd tryffle && docker compose -f docker-compose.${STAGE}.yml down

bash:
	@docker exec -it tryffle_django bash

shell:
	@docker exec -it tryffle_django python manage.py shell

logs:
	@docker logs -ft tryffle_django

upgrade:
	@docker exec -it -u postgres tryffle_postgres psql -U tryffle -c "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
	@docker exec -it tryffle_django python manage.py migrate --noinput
	@docker exec -it tryffle_django python manage.py collectstatic --noinput

init: upgrade
	@docker exec -it tryffle_django python manage.py createsuperuser

# end
