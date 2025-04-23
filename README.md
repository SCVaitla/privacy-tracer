# Privacy Tracer

A lightweight backend tracing tool built with FastAPI to simulate personal data flow tracking across microservices. Ideal for showcasing observability, API logging, and compliance awareness (GDPR-style). Easily extensible for DevOps, privacy tech, or ML infra portfolios.

---

## Features

- Dynamically loads multiple microservices from YAML
- Handles requests across multiple endpoints and HTTP methods
- Tracks personally identifiable fields (PII) such as email, password, payment_info
- Logs all requests to a JSON file for traceability
- Generates aggregated privacy reports via `/report`
- Supports exporting reports as:
  - `/report/markdown` → Markdown `.md` report
  - `/report/html` → Downloadable HTML `.html` report
- Docker-ready for container deployment
- Simple FastAPI homepage and routing

---

## Setup

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run locally with FastAPI

uvicorn app.main:app --reload

App runs at: http://127.0.0.1:8000

---

## Sample Request

Send sample PII data to a configured endpoint:

curl -X POST http://127.0.0.1:8000/order/create \
  -H "Content-Type: application/json" \
  -d '{"name": "Sai", "address": "123 Main St", "payment_info": "Visa"}'

Response:

{
  "message": "Data received at /order/create",
  "tracked": {
    "name": "Sai",
    "address": "123 Main St",
    "payment_info": "Visa"
  }
}

---

## View Reports

- JSON Summary:  
  http://127.0.0.1:8000/report

- Markdown Export:  
  http://127.0.0.1:8000/report/markdown

- HTML Export:  
  http://127.0.0.1:8000/report/html

Files will be saved in the `traces/` folder.

---

## Use Cases

- Privacy compliance prototyping (GDPR, CCPA)
- Secure-by-design backend logging
- Observability & traceability for microservices
- Showcasing dev skills in LLM infra, data flow, or backend safety

---

