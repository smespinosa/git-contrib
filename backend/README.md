# Git Contrib Backend

## Requirements
- Python 3
- Postgres Instance

### Optional
- virtualenv
  
## Installation

```
pip install falcon uvicorn GitPython python-dotenv psycopg[binary]
cp .env-sample .env
```

Configure .env with correct values

## Database

```
docker pull postgres
sh scripts\db\run.sh
```

Run `init.sql` against database

## Run

```
source .venv/bin/activate
uvicorn app:app
```

## Test

`curl http://localhost:8000`