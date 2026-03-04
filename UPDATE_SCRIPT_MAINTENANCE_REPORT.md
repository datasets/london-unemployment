# Update Script Maintenance Report

Date: 2026-03-04

- Updated `scripts/london_unemployment.py` to fetch the source workbook using `requests` with browser-like headers before parsing via pandas.
  - This resolves HTTP 403 failures caused by direct `pandas.read_excel(url)` requests to the London Datastore endpoint.
- Re-ran updater and refreshed:
  - `data/data/unemployment-rate.csv`
  - `data/datapackage.json`
- Updated `scripts/requirements.txt` to modern, installable dependency ranges on current Python versions.
- Modernized workflow automation in `.github/workflows/actions.yml` (schedule/manual triggers, explicit write permissions, current action versions).
