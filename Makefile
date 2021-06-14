# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 app.py

test: venv
	pip install coverage
	coverage run --include=lambda_function.py -m unittest
	coverage report --fail-under=95

lint: venv
	pip install flake8
	flake8 lambda_function.py tests.py

build: test lint

deploy:
	sls deploy

clean:
	rm -rf $(VENV)
	rm -f .coverage
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean