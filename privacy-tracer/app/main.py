from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, FileResponse
from app.config_loader import load_services_config
from app.tracer import trace_request
from app.report_generator import (
    generate_privacy_report,
    generate_markdown_report,
    generate_html_report,
)

app = FastAPI()


# Homepage
@app.get("/")
def home():
    return {"message": "Welcome to the Privacy Tracer!"}


# Load services from config
services = load_services_config()

# Register routes dynamically
for service in services:
    service_name = service.get("name", "unknown-service")
    endpoints = service.get("endpoints", [])
    methods = service.get("methods", [])

    for endpoint in endpoints:
        for method in methods:

            async def handler(
                request: Request,
                endpoint=endpoint,
                service=service_name,
            ):
                return await trace_request(
                    request, service_name=service, endpoint=endpoint
                )

            app.add_api_route(endpoint, handler, methods=[method])


# Report endpoints
@app.get("/report")
def report():
    return generate_privacy_report()


@app.get("/report/markdown", response_class=HTMLResponse)
def markdown_report():
    md = generate_markdown_report()
    return f"<pre>{md}</pre>"


@app.get("/report/html")
def html_report():
    file_path = generate_html_report()
    return FileResponse(
        path=file_path, filename=file_path.split("/")[-1], media_type="text/html"
    )
