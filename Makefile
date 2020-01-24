
.PHONY: black check_black check_format check_isort format isort mypy piptools \
        pylint quality requirements test upgrade upgrade upgrade-piptools \
        upgrade-requirements validate

piptools:
	pip install -r piptools.txt

upgrade-piptools: piptools
	pip-compile --upgrade --rebuild piptools.in -o piptools.txt

requirements: piptools
	pip-sync dev_requirements.txt

upgrade-requirements: piptools
	pip-compile --upgrade --rebuild dev_requirements.in -o dev_requirements.txt
	sed '/^\-e/d' dev_requirements.txt > dev_requirements.tmp
	mv dev_requirements.tmp dev_requirements.txt

upgrade: export CUSTOM_COMPILE_COMMAND=make upgrade
upgrade: upgrade-requirements upgrade-piptools

PYTHON_CODE=*.py untangled

isort:
	isort --recursive $(PYTHON_CODE)

black:
	black  $(PYTHON_CODE)

format_hard: isort black

check_isort:
	isort --recursive --check-only $(PYTHON_CODE)

check_black:
	black --check $(PYTHON_CODE)

format: check_isort check_black

pylint:
	pylint *.py untangled

mypy:
	mypy --check --package untangled

quality: pylint mypy

test:
	pytest untangled

validate: format quality test
	echo '>>>>> Validation complete :) <<<<<'

validate_hard: format_hard quality test
	echo '>>>>> Validation complete :) <<<<<'

provision-tests:
	./provision-tests.sh

clean:
	rm -rf test-data/
