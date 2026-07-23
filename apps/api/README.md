# apps/api

Backend FastAPI local (ADR-002, ADR-004). Capas: `api/` (endpoints) → `services/` (casos de uso) → `confector_core` (dominio) + `confector_database` (repositorios SQLite).

`repositories/` y `database/` de 12§10 no se duplican aquí: ya viven en el paquete reutilizable `packages/database` (12§6), que este servicio consume vía `confector_database`. Evita una segunda capa de acceso a datos redundante.

## Setup (Windows, PowerShell)

```powershell
cd "confector-copilot"
python -m venv .venv
.venv\Scripts\pip install -e packages\core -e packages\database -e ai\models -e packages\exporters -e apps\api
```

## Ejecutar

```powershell
.venv\Scripts\uvicorn app.main:app --reload --app-dir apps\api --port 8000
```

Health check: `GET http://127.0.0.1:8000/health`
