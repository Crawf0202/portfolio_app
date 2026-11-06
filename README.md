# Portfolio App

Will Crawford's portfolio, presented as an interactive file folder with four tabs: **Home Page**, **Projects/Awards**, **Skills** and **Contact**.

This is a dynamic web app, not a static site. Flask renders every page on the server, Gunicorn serves it in production, and it ships as a container on Google Cloud Run. [Bootstrap 5.3](https://getbootstrap.com/) makes it work on desktop, tablet and mobile.

## Stack

| Layer | Tool |
|-------|------|
| Language / dependencies | Python 3.12, Poetry |
| Web framework | Flask (Jinja templates rendered on the server) |
| Production server | Gunicorn |
| Styling | Bootstrap 5.3 from the jsDelivr CDN, plus `static/style.css` |
| Container | `Dockerfile` (multi-stage build) |
| Hosting | Google Cloud Run |

## Routes

| URL | What it returns |
|-----|-----------------|
| `/` | Home Page tab |
| `/projects` | Projects/Awards tab |
| `/skills` | Skills tab |
| `/contact` | Contact tab |
| `/api/portfolio` | All portfolio content as JSON |
| `/healthz` | `{"status": "ok"}` health check |
| anything else | Styled 404 page |

## Run locally

Requirements: Python 3.10 or newer and [Poetry](https://python-poetry.org/docs/#installation).

```bash
poetry install
poetry run python app.py
```

Open http://127.0.0.1:5000. Press `Ctrl+C` to stop it. Add `FLASK_DEBUG=1` in front of the command to reload automatically while you edit.

To run it the way the container does, with Gunicorn:

```bash
poetry run gunicorn --bind 127.0.0.1:8080 app:app
```

## Run the container locally (optional)

Requires [Docker](https://docs.docker.com/get-docker/).

```bash
docker build -t portfolio_app .
docker run --rm -p 8080:8080 portfolio_app
```

Open http://localhost:8080.

## Deploy to Google Cloud Run

Requires the [gcloud CLI](https://cloud.google.com/sdk/docs/install) and a Google Cloud project with billing turned on.

```bash
gcloud auth login
gcloud config set project YOUR_PROJECT_ID
gcloud run deploy portfolio-app --source . --region us-central1 --allow-unauthenticated
```

`--source .` uploads the project, and Cloud Build builds the container from the `Dockerfile` during deployment. The command prints the service URL when it finishes. The first run may ask to turn on the Cloud Run, Cloud Build and Artifact Registry APIs; answer `y`.

Cloud Run service names can't contain underscores, so the service is called `portfolio-app`.

### How the container works

1. **Build stage:** installs Poetry and only the main dependencies (Flask, Gunicorn) into `/app/.venv`, using `poetry.lock`.
2. **Runtime stage:** a clean `python:3.12-slim` image gets the virtualenv and the app files only (see `.dockerignore`). It runs as a non-root user.
3. Gunicorn listens on `0.0.0.0:$PORT`. Cloud Run sets `PORT` (default 8080).

## Screen sizes

| Device | Width | Layout |
|--------|-------|--------|
| Phone | under 768px | One column. The tabs shrink to fit on one row, and Call/Email are full-width buttons |
| Tablet | 768px–1199px | Two columns for projects, facts and contact. Each skill sits next to its level bar |
| Desktop | 1200px and up | Three project cards per row |

## Editing the content

All of the text is in [content.py](content.py):

| Constant | What it holds |
|----------|---------------|
| `PROFILE` | Name, occupation, degree and summary (Home Page) |
| `PROJECTS` | Each project's title, description and tools |
| `SKILLS` | Each skill's name and level (1 = Beginner, 2 = Intermediate, 3 = Expert) |
| `CONTACT` | Phone number and email |

## Project layout

```
app.py              Flask routes, JSON API, health check
content.py          Portfolio content
templates/          Jinja templates (base.html holds the folder and tabs)
static/style.css    Folder theme on top of Bootstrap
Dockerfile          Container build for Cloud Run
.dockerignore       Files kept out of the container
pyproject.toml      Poetry project and dependencies
```
