PYTHON ?= $(if $(wildcard .venv/bin/python),.venv/bin/python,python3)
SOLUTIONS := $(wildcard [0-9]*.py)
PROBLEMS := $(patsubst %.py,%,$(SOLUTIONS))
ALIASES := 11 33 36 128 153 167 238 347 42 424

.PHONY: test $(PROBLEMS) $(ALIASES)

test:
	$(PYTHON) -m pytest --import-mode=importlib $(SOLUTIONS) -v

$(PROBLEMS):
	$(PYTHON) -m pytest --import-mode=importlib $@.py -v

0011: 0011
0033: 0033
0036: 0036
0128: 0128
0153: 0153
0167: 0167
0217: 0217
0238: 0238
0347: 0347
0042: 0042
0560: 0560
0746: 0746
