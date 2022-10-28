run:
	uvicorn app.main:app --port 8080 --reload

migrate:
	@venv/bin/alembic upgrade head