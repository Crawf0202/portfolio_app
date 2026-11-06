# Plan: Portfolio app with folder-style tabs (Flask)

## Context
The repo is empty apart from `CLAUDE.md`. Will wants a personal portfolio app shown as an interactive file folder with four tabs: Home Page, Projects/Awards, Skills and Contact. Following `CLAUDE.md`, it uses Python with Poetry, keeps dependencies to a minimum (Flask only), uses underscore names and doesn't touch `main`.

## Steps (in order)
1. **Prompt log**: create `PROMPTS.md` and add a time-stamped entry for this prompt.
2. **Save the plan**: copy this plan to `plans/01_portfolio_folder_tabs.md`.
3. **Branch**: `git checkout -b portfolio_folder_tabs` (never work on `main`; no commits).
4. **Poetry project**: write `pyproject.toml` (package-mode = false, Python ^3.10, dependency `flask`). Run `poetry install`.
5. **App files**:
   - `app.py`: a Flask app with one `/` route that renders `templates/index.html`. The portfolio content lives in Python dicts/lists (`PROFILE`, `PROJECTS`, `SKILLS`, `CONTACT`) and is passed to the template, so editing content never means editing HTML. Runs on `127.0.0.1:5000` with `debug` turned on only through an env var.
   - `templates/index.html`: a Jinja template. A row of folder tabs (buttons with `role="tab"` and ARIA attributes) sits above one manila "folder body" panel per section.
   - `static/style.css`: manila folder look (tabs with rounded tops, the active tab merges into the folder body, paper texture/shadow, responsive down to phone width).
   - `static/script.js`: tiny tab switcher (click and arrow-key navigation; updates the URL hash so `#skills` deep-links to that tab).
6. **Content**:
   - **Home Page**: Will Crawford · Automation Specialist · Electrical and Computer Eng Technology · the summary, with spelling fixed ("an automation specialist", "fulfillment").
   - **Projects/Awards**: 3 made-up DevOps projects, each with a title, description and technology/tools tags:
     1. *PLC Code CI Pipeline*: version control and automated checks for Rockwell Studio 5000 L5X exports (Git, GitHub Actions, Python, Docker).
     2. *Plant Floor Telemetry Stack*: containerized collection of OPC UA/MQTT drive and PLC data with dashboards and alerts (Docker Compose, MQTT, InfluxDB, Grafana, Ansible).
     3. *Infrastructure-as-Code for Edge Gateways*: reproducible provisioning and rolling updates of plant-floor edge devices (Terraform, Ansible, Prometheus, GitLab CI).
   - **Skills**: 6 skills, each with a 3-step level meter (Beginner / Intermediate / Expert: filled segments plus a text label so it doesn't rely on colour alone), using the levels given.
   - **Contact**: phone as a `tel:` link and email as a `mailto:` link.
7. **README.md**: prerequisites (Python 3.10+, Poetry), `poetry install`, `poetry run python app.py`, then open http://127.0.0.1:5000. Briefly note where to edit the content in `app.py`.
8. **.gitignore**: `__pycache__/`, `.venv/`, `.env`.

## Files created
`PROMPTS.md`, `plans/01_portfolio_folder_tabs.md`, `pyproject.toml` (+ `poetry.lock`), `app.py`, `templates/index.html`, `static/style.css`, `static/script.js`, `README.md`, `.gitignore`

## Verification
- `poetry install`, then `poetry run python app.py` starts the app without errors.
- `curl -s http://127.0.0.1:5000/` returns HTML that contains all four section titles, the name, all 3 projects, all 6 skills and the contact details.
- `curl` the static CSS and JS to confirm they return 200.
- Check by hand in a browser: clicking a tab switches folders, arrow keys work, `#skills` opens Skills, and the layout holds at phone width.
- `git branch --show-current` shows `portfolio_folder_tabs`, and nothing is committed.
