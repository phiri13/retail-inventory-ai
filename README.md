# RetailAI-ZA 🛒📊

>  API for retail inventory forecasting using Prophet time-series models

[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green.svg)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 🎯 Overview

Production-ready  API for forecasting retail product demand across multiple stores. Built with FastAPI, Prophet, and containerized for cloud deployment.

**Key Features:**
- RESTful API with versioned endpoints (`/v1/`)
- Prophet time-series forecasting engine
- Disk-based model registry with metadata tracking
- Docker containerization for reproducible deployments
- OpenAPI/Swagger documentation

## 🚀 Quick Start

### Using Docker (Recommended)
```bash
# Build and start the API
docker-compose up --build

# API available at http://localhost:8000
# Docs at http://localhost:8000/docs
```

### Local Development
```bash
# Install dependencies
pip install -r requirements.txt

# Start the API
python -m uvicorn api.main:app --reload --app-dir src

# Access at http://localhost:8000
```

## 📡 API Endpoints

### Health Check
```bash
GET /v1/health
```

### Generate Forecast
```bash
POST /v1/forecast
Content-Type: application/json

{
  "store_id": "default",
  "product_id": "generic",
  "days": 30
}
```

**Response:**
```json
{
  "store_id": "default",
  "product_id": "generic",
  "horizon_days": 30,
  "forecasts": [
    {"date": "2026-01-06", "forecast": 185.4},
    {"date": "2026-01-13", "forecast": 192.1},
    ...
  ]
}
```

## 🏗️ Architecture
```
retail-inventory-ai/
├── src/
│   ├── api/
│   │   ├── main.py              # FastAPI app
│   │   ├── schemas.py           # Pydantic models
│   │   └── v1/
│   │       ├── health.py        # Health endpoint
│   │       └── forecast.py      # Forecast endpoint
│   └── models/
│       ├── registry/            # Model storage
│       ├── load_model.py        # Model loader
│       └── train_prophet.py     # Training script
├── data/
│   └── raw/                     # Training data
├── Dockerfile                   # Container definition
├── docker-compose.yml           # Local orchestration
└── requirements.txt             # Python dependencies
```

## 🧠 Model Registry Design

Models are stored in a hierarchical structure:
```
src/models/registry/
└── store={store_id}/
    └── product={product_id}/
        ├── model.pkl           # Serialized Prophet model
        └── metadata.json       # Model metadata
```

**Metadata includes:**
- Model type and version
- Training data statistics
- Supported forecast horizon
- Frequency (daily/weekly)

## 🛠️ Tech Stack

- **API Framework:** FastAPI 0.115
- **ML Model:** Facebook Prophet 1.1.5
- **Data Processing:** Pandas, NumPy
- **Containerization:** Docker, docker-compose
- **Validation:** Pydantic v2

## 📦 Deployment

### Docker
See [README_DOCKER.md](README_DOCKER.md) for detailed Docker deployment instructions.

### Cloud Platforms
This API is compatible with:
- **AWS:** ECS, Fargate, Lambda (with container support)
- **GCP:** Cloud Run, GKE
- **Azure:** Container Apps, AKS

## 🧪 Testing the API

### Via Swagger UI
Navigate to `http://localhost:8000/docs` for interactive API documentation.

### Via curl
```bash
curl -X POST "http://localhost:8000/v1/forecast" \
  -H "Content-Type: application/json" \
  -d '{
    "store_id": "default",
    "product_id": "generic",
    "days": 7
  }'
```

## 📈 Future Enhancements

- [ ] Model versioning and A/B testing
- [ ] CI/CD pipeline (GitHub Actions)
- [ ] Unit tests with pytest
- [ ] Prometheus metrics and monitoring
- [ ] Multi-model support (ARIMA, LSTM)
- [ ] Database integration for model metadata

## 📝 License

MIT License - see [LICENSE](LICENSE) for details.

## 👤 Author

**Joshua Phiri**
- GitHub: [@phiri13](https://github.com/phiri13)
- Project: [retail-inventory-ai](https://github.com/phiri13/retail-inventory-ai)

---


