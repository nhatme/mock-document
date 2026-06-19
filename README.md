# Usage

Build the financial advisor report with `make`.

## Requirements

- Python 3
- `make`

## Commands

```sh
make            # diagrams + build report (default)
make venv       # create/update docxenv/ venv from requirements.txt
make diagrams   # regenerate diagrams/*.png
make report     # regenerate diagrams, then build the .docx report
make clean      # remove generated outputs (docx, pdf, preview pngs, cache json, log)
```

The venv is created automatically on first run; re-running `make` reuses it.

Output `.docx` path is set by `OUT_PATH` in `build_report.py`.
