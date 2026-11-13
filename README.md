# Job Application Tracker API

A Django REST API for tracking job applications: companies, applications, interviews and notes,
with JWT auth, stats, follow-up reminders (Celery) and an optional AI job-match feature.

## Stack
Python 3.11+ · Django · Django REST Framework · PostgreSQL · Redis · Celery · Docker · pytest

## Local setup (Windows, PowerShell)
```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements/dev.txt
copy .env.example .env        # then fill in real values
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

## Project layout
See [STRUCTURE.md](STRUCTURE.md).

## Levels
- [ ] 1. Django basics: models + admin
- [ ] 2. REST API with DRF
- [ ] 3. JWT auth + per-user data
- [ ] 4. Stats endpoint (ORM vs raw SQL)
- [ ] 5. Docker
- [ ] 6. Celery reminders
- [ ] 7. Tests + CI
- [ ] 8. AI job match (optional)
