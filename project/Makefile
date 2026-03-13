up:
	docker compose up --build

down:
	docker compose down --remove-orphans

logs:
	docker compose logs -f --timestamps

ps:
	docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"

test:
	docker build -t todo-api:test --target builder api
	docker run --rm todo-api:test poetry run pytest -q
	docker run --rm -v "$(PWD)/frontend:/app" -w /app node:20-alpine npm test

scan:
	mkdir -p reports
	trivy image --format table --output reports/todo-api-trivy.txt todo-api:latest
	trivy image --format cyclonedx --output reports/todo-api.bom.json todo-api:latest
