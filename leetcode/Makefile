PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
SOLUTIONS := $(wildcard [0-9]*.py)
PROBLEMS := $(patsubst %.py,%,$(SOLUTIONS))
ALIASES := 11 33 36 128 153 167 238 347 42 424

.PHONY: test $(PROBLEMS) $(ALIASES)

test:
	$(PYTHON) -m pytest --import-mode=importlib $(SOLUTIONS) -v

$(PROBLEMS):
	$(PYTHON) -m pytest --import-mode=importlib $@.py -v

11: 0011
33: 0033
36: 0036
128: 0128
153: 0153
167: 0167
238: 0238
347: 0347
42: 0042
424: 0424
