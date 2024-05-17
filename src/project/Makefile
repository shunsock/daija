.PHONY: all formatting linting static-analysis test report

all: formatting linting static-analysis test report

project_name = project
test_dir = tests

formatting:
	poetry run isort $(project_name) $(test_dir)
	poetry run black $(project_name) $(test_dir)

linting:
	poetry run flake8 $(project_name) $(test_dir)

static-analysis:
	poetry run mypy $(project_name) $(test_dir)

test:
	poetry run coverage run -m pytest --durations=10

report:
	poetry run coverage report -m