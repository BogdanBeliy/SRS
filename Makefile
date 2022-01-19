BACK_CONTAINER=sr_back
DATABASE_CONTAINER_NAME=sr_db

mkm: ## make migrations
	docker exec -it ${BACK_CONTAINER} python manage.py makemigrations

m: ## migrate
	docker exec -it ${BACK_CONTAINER} python manage.py migrate

drop_db:
	docker exec -it ${BACK_CONTAINER} python manage.py flush

csu: ## create superuser
	docker exec -it ${BACK_CONTAINER} python manage.py createsuperuser

exec: ## exec back container
	docker exec -it ${BACK_CONTAINER} bash

exec_db: ## exec db container
	docker exec -it ${DATABASE_CONTAINER_NAME} bash
