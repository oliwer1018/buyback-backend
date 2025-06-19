# BuyBack Backend

This is a backend system for processing device buyback assessments, handling SKU matching, pricing logic, defect
deductions, and async task management.

---

## 🛠 Tech Stack

- **Django** – Admin & ORM
- **FastAPI** – REST API endpoints
- **Celery** – Background task queue
- **PostgreSQL** – Database
- **Docker** – Containerized local dev
- **Redis** – Celery broker
- **Python 3.11+**

---

## 🚀 Getting Started Locally

You can run the project either via Docker or manually using a virtual environment.

### ▶️ Option 1: Dockerized Setup

#### 1. Clone the repository

```
git clone https://github.com/oliwer1018/buyback-backend.git
cd buyback-backend
```

#### 2. Create .env file

```
cp .env.example .env  # or create your own and edit values
```

#### 3. Run everything (Django, FastAPI, PostgreSQL, Redis, Celery)

```
docker-compose up --build
```

**Endpoints Available:**

- FastAPI: [http://localhost:8000](http://localhost:8000)
- Django Admin: [http://localhost:8001/admin](http://localhost:8001)


#### 5. Run Servers

# Django admin (port 8001)

```python manage.py runserver 8001```


# FastAPI app (port 8000)

```uvicorn app.main:app --reload --port 8000```

# Celery worker

```
celery -A app.tasks worker --loglevel=info
```

---

## 📄 Environment Variables

| Variable          | Description                  |
|-------------------|------------------------------|
| POSTGRES_DB       | Database name                |
| POSTGRES_USER     | DB user                      |
| POSTGRES_PASSWORD | DB password                  |
| DB_HOST           | Usually \`db\` in Docker     |
| REDIS_URL         | For Celery (\`redis://...\`) |
| DJANGO_SECRET_KEY | Django security key          |

---

## 📦 CSV Bootstrapping

On first run, Django will load:

- \`mock_sku_list_1000.csv\`
- \`defect_deduction_matrix.csv\`

These files are used to populate SKU and defect data automatically on app init.

---

## 🔁 Key Endpoints

- \`POST /submit-assessment/\` – Submit device data for pricing
- \`GET /pricing-status/{task_id}/\` – Check async pricing result
- Django Admin Panel – Manage SKUs, devices, and more

---

## ✅ Tests

\`\`\`bash
pytest
\`\`\`

---

## 🧩 Bonus Features (Included)

- ✅ Celery task queue
- ✅ CSV auto-load
- ✅ Modular pricing logic
- ✅ Docker support
- 🚧 API key-level evaluator auth (optional)

---

## 📬 Contributing

Pull requests welcome. Please open issues for feature suggestions or bugs.
