# Project structure

Every file already exists. Stub files hold a docstring saying what goes in them, which level fills
them in, and `# TODO` hints. Write the code yourself, level by level. Leave a file as a stub until
you reach its level.

```
jobtracker/
├── manage.py                    Django CLI (defaults to config.settings.dev)
├── .env.example                 every env var the app reads; copy to .env
├── requirements/
│   ├── base.txt                 needed everywhere
│   ├── dev.txt                  + test tools
│   └── prod.txt                 + gunicorn
├── config/                      project package: settings, urls, wsgi, celery
│   ├── settings/
│   │   ├── base.py              shared settings                     L1
│   │   ├── dev.py               local                               L1
│   │   ├── test.py              pytest                              L7
│   │   └── prod.py              production                          L5
│   ├── urls.py                  root URLs                           L1
│   ├── wsgi.py / asgi.py        server entry points
│   └── celery.py                Celery app + Beat schedule          L6
├── apps/                        all Django apps live here
│   ├── core/                    shared pieces, no tables of its own
│   │   ├── models.py            TimeStampedModel (abstract)         L1
│   │   ├── pagination.py        page size rules                     L2
│   │   ├── exceptions.py        one JSON error format               L2
│   │   └── permissions.py       IsOwner                             L3
│   ├── accounts/                custom User + auth API
│   │   ├── models.py            User(AbstractUser)                  L1
│   │   ├── admin.py                                                 L1
│   │   ├── api/                 register, me, JWT urls              L3
│   │   └── tests/                                                   L7
│   ├── tracker/                 the main feature app
│   │   ├── models/              one file per model + choices.py     L1
│   │   ├── admin.py             admin with inlines                  L1
│   │   ├── api/                 serializers, views, filters, urls   L2
│   │   ├── services/            logic that changes data             L2, L6
│   │   ├── queries/             stats: ORM and raw SQL              L4
│   │   ├── tasks.py             Celery tasks                        L6
│   │   ├── management/commands/seed_demo.py   sample data           L1 (optional)
│   │   └── tests/               factories + tests                   L7
│   └── matching/                AI job match                        L8
├── templates/emails/            reminder email templates            L6
├── docker/                      Dockerfile, entrypoint, gunicorn    L5
├── docker-compose.yml           web + db + redis (+ celery)         L5
├── docker-compose.dev.yml       dev overrides                       L5
├── .github/workflows/ci.yml     run tests on every push             L7
├── docs/                        architecture, API, decisions
└── logs/                        log files (ignored by git)
```

## The rules this layout follows

1. **Thin views.** `api/views.py` only handles HTTP. Rules like "changing status to Interview sets
   first_response_on" go in `services/`, so the API, admin actions and Celery tasks all reuse them.
2. **Reads and writes are separate.** `services/` changes data; `queries/` only reads it (stats).
3. **Small files.** One model per file, one concern per module. If a file passes ~300 lines, split it.
4. **Settings per environment.** `base.py` holds what's shared; dev, test and prod only override.
5. **No secrets in the repo.** Everything secret comes from `.env`; `.env.example` lists the keys.
6. **Tests live inside each app** in a `tests/` package, never loose at the app root.

## Ideas taken from RADIUM (structure only, no code)

- A feature package organised like RADIUM's newer analytics module: `apps.py`, `urls.py`,
  `tasks.py`, plus `views/`, `services/` and `queries/` folders.
- A project package holding settings, urls, wsgi/asgi and `celery.py` together.
- Separate docker-compose files for dev and production, a Gunicorn config and a container start script.
- A `docs/` folder and a CI pipeline file at the root.

## Things RADIUM does that this project avoids

- One app with 60+ loose modules at its root. Here, features are split into separate apps and folders.
- Version suffixes in file names (`serializers1.py`, `*_old.py`). Git keeps the history instead.
- Tokens, logs, trained models and `__pycache__` inside the source tree. `.gitignore` blocks them.
- Test files mixed in with application code. Here, tests go in `tests/` folders.
- A single settings file for every environment.
- Deep nesting (`backend/backend/api/server/app`). Here, `manage.py` sits at the root.

## Level 1 with this layout

Skip `startproject` and `startapp`: the files already exist. Because the apps are inside `apps/`:

- `INSTALLED_APPS` uses `"apps.accounts"` and `"apps.tracker"` (and `"apps.core"`).
- `AUTH_USER_MODEL = "accounts.User"` uses the app **label**, not the dotted path.
- In `base.py`, `BASE_DIR = Path(__file__).resolve().parent.parent.parent` (three levels up, since
  settings now sit in `config/settings/`).
- Add `apps.matching` to `INSTALLED_APPS` only when you reach Level 8.
