# CI/CD + Kubernetes demo
Flask app -> GitHub Actions (test, build, push to GHCR) -> kubectl deploy.

Run locally:  pip install -r requirements.txt && pytest && python app.py
