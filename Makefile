up:
	docker compose up -d

down:
	docker compose down

make import:
	docker exec -it web poetry run python source/import.py
