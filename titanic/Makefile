PYTHON ?= python

.PHONY: requirements
requirements:
	$(PYTHON) -m pip install -r requirements.txt

.PHONY: docs
docs:
	$(MAKE) -C docs html
