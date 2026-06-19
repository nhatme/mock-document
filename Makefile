VENV := docxenv
PYTHON := $(VENV)/bin/python

.PHONY: all venv diagrams report clean

all: report

venv:
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PYTHON) -m pip install -q -r requirements.txt

diagrams: venv
	$(PYTHON) make_diagrams.py

report: diagrams
	$(PYTHON) build_report.py

clean:
	rm -f *.docx *.pdf cover*.png page*.png toc_page.png toc_page_map.json soffice.log
