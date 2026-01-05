## Deployment

This project is containerized and deployment-ready:

- **Docker**: `docker-compose up` (see [README_DOCKER.md](README_DOCKER.md))
- **Cloud**: Compatible with AWS ECS, GCP Cloud Run, Azure Container Apps
- **Local**: `python -m uvicorn api.main:app --reload --app-dir src`
