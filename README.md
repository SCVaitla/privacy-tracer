# Privacy Tracer

A lightweight FastAPI-based tool that **traces personal data flow across microservices** and generates audit-friendly reports. Built for developers and privacy teams to simulate GDPR/CCPA-style compliance logging in distributed systems.

---

##  Features

- Simulate API endpoints across multiple microservices
- Track sensitive fields like `email`, `password`, `payment_info`, etc.
- Log every request with timestamp, service name, and endpoint
- View aggregated privacy reports via a `/report` endpoint
- Export reports as **Markdown** or **HTML**
- Dockerized for easy deployment

---

## Project Structure

