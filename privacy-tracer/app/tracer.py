import json
import os
from datetime import datetime
from fastapi import Request

LOG_FILE = "data/trace_log.json"


async def trace_request(request: Request, service_name: str, endpoint: str):
    body = await request.json()

    # Load YAML config
    from app.config_loader import load_services_config

    services = load_services_config()

    # Get tracked fields for the current service
    tracked_fields = []
    for service in services:
        if service["name"] == service_name:
            tracked_fields = service.get("tracks", [])
            break

    # Filter only tracked fields from the request body
    tracked_data = {key: body.get(key) for key in tracked_fields if key in body}

    # Build trace log entry
    trace_entry = {
        "timestamp": datetime.now().isoformat(),
        "service": service_name,
        "endpoint": endpoint,
        "fields": tracked_data,
    }

    # Safely load existing logs or start fresh
    if os.path.exists(LOG_FILE) and os.path.getsize(LOG_FILE) > 0:
        with open(LOG_FILE, "r") as f:
            existing_logs = json.load(f)
    else:
        existing_logs = []

    # Append new entry
    existing_logs.append(trace_entry)

    # Write back to file
    with open(LOG_FILE, "w") as f:
        json.dump(existing_logs, f, indent=2)

    return {"message": f"Data received at {endpoint}", "tracked": tracked_data}
