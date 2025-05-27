# 🧠 Litigation MLOps

A containerized machine learning application that predicts litigation outcomes using a trained scikit-learn model, exposed via a FastAPI interface and Dockerized for seamless deployment.

---

## 📦 Features

- 📊 Predicts case outcomes (Win/Loss) using basic case details
- ⚡ FastAPI backend for clean REST API
- 🐳 Dockerized for consistent deployment
- 🤖 Pretrained scikit-learn model included
- 🔁 CI/CD enabled with GitHub Actions
- 🧪 Local dev & testing with `uvicorn`, `pytest`

---

## 🚀 Docker Hub

Image is publicly available on Docker Hub:  
🔗 [https://hub.docker.com/r/eddy35/litigation-mlops](https://hub.docker.com/r/eddy35/litigation-mlops)

### 🐳 Run from Docker Hub

```bash
docker pull eddy35/litigation-mlops
docker run -d -p 8000:8000 eddy35/litigation-mlops
```

---

## 📡 API Usage

Once running, you can POST to the `/predict` endpoint:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"case_number": "12345", "plaintiff": "John Doe", "defendant": "Jane Smith"}'
```

### ✅ Sample Response:

```json
{
  "prediction": "loss"
}
```

---

## 🧪 Local Development

### 🔧 Setup

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### ▶️ Run Locally

```bash
uvicorn api.app:app --reload
```

### 🧪 Run Tests

```bash
pytest
```

---

## ⚙️ CI/CD Pipeline

This project includes a GitHub Actions workflow:

- ✅ Lints and tests on push
- 🐳 Builds the Docker image
- 🚀 Supports Docker Hub publishing (manual)

---

## 📝 License

MIT License © 2025  
