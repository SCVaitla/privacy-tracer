import json
import os
from pathlib import Path
from collections import defaultdict

TRACE_LOG_PATH = Path("data/trace_log.json")
REPORT_DIR = Path("traces")
REPORT_DIR.mkdir(exist_ok=True)


def generate_privacy_report():
    report = defaultdict(set)

    if not TRACE_LOG_PATH.exists():
        return {}

    with open(TRACE_LOG_PATH, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            return {}

    for entry in data:
        endpoint = entry.get("endpoint", "unknown")
        fields = entry.get("fields", {})
        for field in fields:
            report[endpoint].add(field)

    # Convert sets to lists for JSON serialization
    return {ep: list(fields) for ep, fields in report.items()}


def generate_markdown_report():
    report = generate_privacy_report()
    lines = ["# Privacy Data Flow Report\n"]

    for endpoint, fields in report.items():
        lines.append(f"## Endpoint: `{endpoint}`")
        lines.append("- Fields Tracked:")
        for field in fields:
            lines.append(f"  - `{field}`")
        lines.append("")  # blank line between sections

    output_path = REPORT_DIR / "report.md"
    with open(output_path, "w") as f:
        f.write("\n".join(lines))

    return str(output_path)


def generate_html_report():
    report = generate_privacy_report()
    html = ["<html><head><title>Privacy Report</title></head><body>"]
    html.append("<h1>Privacy Data Flow Report</h1>")

    for endpoint, fields in report.items():
        html.append(f"<h2>Endpoint: <code>{endpoint}</code></h2>")
        html.append("<ul>")
        for field in fields:
            html.append(f"<li><code>{field}</code></li>")
        html.append("</ul>")

    html.append("</body></html>")

    output_path = REPORT_DIR / "report.html"
    with open(output_path, "w") as f:
        f.write("\n".join(html))

    return str(output_path)
