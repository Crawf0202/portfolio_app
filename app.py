"""Will Crawford's portfolio: a Flask web app presented as an interactive file folder.

Every folder tab is its own server-rendered route. The app also serves a JSON API
and a health check, and runs under Gunicorn in a container on Google Cloud Run.
"""

import os
from datetime import datetime, timezone

from flask import Flask, jsonify, render_template, request

from content import CONTACT, LEVELS, PROFILE, PROJECTS, SKILLS

app = Flask(__name__)

# Folder tabs, in display order: (endpoint, label).
TABS = [
    ("home", "Home Page"),
    ("projects", "Projects/Awards"),
    ("skills", "Skills"),
    ("contact", "Contact"),
]


def skill_rows():
    """Add the label and meter width for each skill, so templates stay simple."""
    top = max(LEVELS)
    return [
        {
            **skill,
            "label": LEVELS[skill["level"]],
            "percent": round(skill["level"] * 100 / top),
            "is_top": skill["level"] == top,
        }
        for skill in SKILLS
    ]


@app.context_processor
def shared_context():
    """Values every page needs: the tabs, the active tab and the profile."""
    return {
        "tabs": TABS,
        "active": request.endpoint,
        "profile": PROFILE,
        "year": datetime.now(timezone.utc).year,
    }


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/projects")
def projects():
    return render_template("projects.html", projects=PROJECTS)


@app.route("/skills")
def skills():
    return render_template("skills.html", skills=skill_rows(), levels=LEVELS)


@app.route("/contact")
def contact():
    phone_link = "tel:+1" + CONTACT["phone"].replace("-", "")
    return render_template("contact.html", contact=CONTACT, phone_link=phone_link)


@app.route("/api/portfolio")
def api_portfolio():
    """All portfolio content as JSON."""
    return jsonify(
        profile=PROFILE,
        projects=PROJECTS,
        skills=skill_rows(),
        contact=CONTACT,
    )


@app.route("/healthz")
def healthz():
    """Health check for Cloud Run and load balancers."""
    return jsonify(status="ok")


@app.errorhandler(404)
def not_found(_error):
    return render_template("not_found.html"), 404


if __name__ == "__main__":
    # Local development only. In the container, Gunicorn serves the app (see Dockerfile).
    port = int(os.environ.get("PORT", "5000"))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="127.0.0.1", port=port, debug=debug)
