APP = deltareeboque

test:
	@flake8 . --exclude .venv

run:
	@docker compose up -d
	@python3 manage.py runserver