# Resume Screening Agent

A Python FastAPI backend for a resume screening agent.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

The API documentation is available at `http://127.0.0.1:8000/docs`.

## Run tests

```bash
pytest
```

## Main endpoints

- `GET /` - application status
- `GET /api/health` - service health
- `POST /api/screenings` - create a placeholder resume screening result
