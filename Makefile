.PHONY: test

virtualenv:
	virtualenv --python=python3.7.10 --prompt '|> [HA_API_V5] <| ' env  --no-download
	env/bin/pip install --upgrade setuptools pip
	env/bin/pip install -r requirements.dev.txt

	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

pretty:
	@echo ♥ ♥ ♥
	python -m isort --atomic helloasso_apiv5/ tests/
	python -m black .

quality:
	python -m flake8 --max-complexity 10 --ignore E501,Q000,S101,DAR201,DAR002,D205,C812,C813 --extend-exclude=tests/,venv/,env/,build/ .

validity:
	python -m flake8 --count --select=E9,F63,F7,F82 --show-source --statistics --extend-exclude=tests/,venv/,env/,build/ .

test:
	python -m pytest --cov-branch tests --cov=helloasso_apiv5 --cov-report=html:htmlcov
	@echo report available at http://localhost:63342/public_api/htmlcov/index.html?_ijt=d27hu38tr1qe74rnp8b76lc4cd