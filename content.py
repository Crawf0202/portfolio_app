"""Portfolio content. Edit these values to change what the site shows."""

PROFILE = {
    "name": "Will Crawford",
    "occupation": "Automation Specialist",
    "degree": "Electrical and Computer Eng Technology",
    "summary": (
        "I am currently an automation specialist assisting manufacturers with "
        "automation solutions needed to keep manufacturing processes going. I "
        "specialize in limiting downtime and increasing plant visibility through "
        "modern communication protocols and advanced Rockwell systems designed "
        "for predictive maintenance. My goal in pursuing the MBT degree is to "
        "become a manager and guide other specialists towards a path of both "
        "mastery and fulfillment."
    ),
}

PROJECTS = [
    {
        "title": "PLC Code CI Pipeline",
        "description": (
            "Brought version control and automated checks to PLC programs. "
            "Studio 5000 projects are exported as L5X files, committed to Git, "
            "and checked on every change by a pipeline that flags naming-rule "
            "violations, unused tags and edits to safety routines before code "
            "reaches the plant floor."
        ),
        "tools": ["Git", "GitHub Actions", "Python", "Docker", "Studio 5000"],
    },
    {
        "title": "Plant Floor Telemetry Stack",
        "description": (
            "A containerized monitoring stack that collects drive and PLC data "
            "over OPC UA and MQTT, stores it as time-series data, and shows "
            "dashboards and alerts for motor current, temperature and fault "
            "trends so maintenance can act before a line goes down."
        ),
        "tools": ["Docker Compose", "MQTT", "OPC UA", "InfluxDB", "Grafana", "Ansible"],
    },
    {
        "title": "Infrastructure as Code for Edge Gateways",
        "description": (
            "Replaced hand-built plant-floor edge devices with reproducible "
            "provisioning. New gateways are set up from code in minutes, "
            "updates roll out in stages with automatic rollback, and every "
            "device reports its health to a central monitor."
        ),
        "tools": ["Terraform", "Ansible", "GitLab CI", "Prometheus", "Linux"],
    },
]

# Skill level is a number from 1 to 3; LEVELS gives its label.
LEVELS = {1: "Beginner", 2: "Intermediate", 3: "Expert"}

SKILLS = [
    {"name": "Python Programming", "level": 2},
    {"name": "Variable Frequency Drives Fundamental Knowledge", "level": 3},
    {"name": "Functional Safety for Machinery", "level": 2},
    {"name": "Variable Frequency Drive Programming and Troubleshooting", "level": 3},
    {"name": "Industrial Controls and Industrial Safety Components", "level": 2},
    {"name": "PLC Programming", "level": 2},
]

CONTACT = {
    "phone": "762-998-7865",
    "email": "wkcrawfo@purdue.edu",
}
