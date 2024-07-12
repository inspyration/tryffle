#
# Tryffle
#
# Only for local development
MAKEFLAGS+="-j 2"

up:
	@cd tryffle && docker compose up -d

down:
	@cd tryffle && docker compose down

bash:
	@docker exec -it tryffle_django bash

shell:
	@docker exec -it tryffle_django python manage.py shell

upgrade:
	@docker exec -it -u postgres tryffle_postgres psql -U tryffle -c "CREATE EXTENSION IF NOT EXISTS pg_trgm;"
	@docker exec -it tryffle_django python manage.py migrate
	@docker exec -it tryffle_django python manage.py collectstatic --noinput

init: upgrade
	@docker exec -it tryffle_django python manage.py createsuperuser

# end
