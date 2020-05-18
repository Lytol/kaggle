PYTHON ?= python

.PHONY: setup
setup:
	$(PYTHON) -m pip install --upgrade pip setuptools wheel
	$(PYTHON) -m pip install -e .

.PHONY: requirements
requirements:
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: docs
docs:
	$(MAKE) -C docs html

.PHONY: jupyter
jupyter:
	$(PYTHON) -m jupyter notebook --notebook-dir=notebooks
