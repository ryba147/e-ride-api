run:
	uvicorn app.main:app --reload

format-code:
	venv/bin/python -m black app/