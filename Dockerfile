FROM resero/python-poetry
COPY . /python-hello-world
WORKDIR /python-hello-world/
RUN poetry install
RUN poetry run flake8 hello_world.py
RUN poetry run pytest tests/unit_tests.py