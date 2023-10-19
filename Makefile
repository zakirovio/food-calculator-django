up:
	docker compose up -d

down:
	docker compose down

import:
	docker exec -it web poetry run python source/import.py

stop:
	docker stop web db

start:
	docker start db web

dotenv:
	 cat source/config/.env.template > source/config/.env
