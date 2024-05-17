# Daija
## Project Overview
Daija is a boilerplate setup for Python projects, equipped with tools for development, testing, and maintaining code quality. This setup leverages Docker for containerization and Poetry for dependency management.

## Prerequisites
Before you begin, ensure you have the following software installed:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Getting Started

### Build
To build the Docker containers, run the following command:
```shell
docker compose up -d --build
```

### Get into container
To get into the application container, use the following command:
```shell
docker compose exec app bash
```

### Initialize
Once inside the container, initialize the project dependencies with Poetry:
```shell
~app/project$ poetry install
```

### Run Workflow
We can run formatting, linting, and other kinds of workflows before executing the Python script using the Makefile. The Makefile handles the following tasks:

- Formatting: isort, black
- Linting: flake8
- Static Analysis: mypy
- Testing: pytest
- Reporting: coverage

To execute the workflows, run:
```shell
~app/project$ make
```
Example output:
```shell
root@dc6e8ed678a6:~/opt/src/project# make
poetry run isort project tests
poetry run black project tests
All done! ✨ 🍰 ✨
4 files left unchanged.
poetry run flake8 project tests
poetry run mypy project tests
Success: no issues found in 4 source files
poetry run coverage run -m pytest --durations=10
======================================================== test session starts =========================================================
platform linux -- Python 3.12.3, pytest-8.2.0, pluggy-1.5.0
rootdir: /root/opt/src/project
configfile: pyproject.toml
collected 1 item                                                                                                                     

tests/test_main.py .                                                                                                           [100%]

======================================================== slowest 10 durations ========================================================

(3 durations < 0.005s hidden.  Use -vv to show these durations.)
========================================================= 1 passed in 0.06s ==========================================================
poetry run coverage report -m
Name                  Stmts   Miss  Cover   Missing
---------------------------------------------------
project/__init__.py       0      0   100%
project/main.py           2      0   100%
tests/__init__.py         0      0   100%
tests/test_main.py        3      0   100%
---------------------------------------------------
TOTAL                     5      0   100%
```

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes. Make sure to follow the established code style and include tests for new features.

## Contact
For questions or support, please open an issue in the repository or contact s.tsuchiya.business@gmail.com
