
# 🧴 Perfume API (Django REST Framework)

A Django REST Framework backend for managing perfume products with JWT and session authentication, Postgres database, filtering, and role-aware permissions via a custom user model.

---

## 🎯 Overview

- Django 5 + DRF for REST APIs
- Auth: JWT (SimpleJWT), Session, and DRF Token (Bearer)
- PostgreSQL database
- Custom user model with roles: admin, manager, customer
- Filtering, searching, ordering on product endpoints
- Optional Algolia indexing (requires extra dependencies)

---

## ⚙️ Quick Start

### 1) Python and virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install -r requirements.txt
```

If you keep Algolia integration enabled (see `INSTALLED_APPS`), also install:
```bash
pip install algoliasearch-django algoliasearch
```

### 3) Environment variables

Create a `.env` file in the repository root:

```dotenv
SECRET_KEY=your_secret_key

# PostgreSQL
DATABASE_NAME=your_db_name
DATABASE_USER=your_db_user
DATABASE_PASSWORD=your_db_password
DATABASE_HOST=localhost
DATABASE_PORT=5432

# Optional: Algolia (only if you enable search indexing)
APPLICATION_ID=your_algolia_app_id
API_KEY=your_algolia_admin_api_key
```

Notes:
- `DEBUG` is currently set to `True` in settings. For production, update `DEBUG` and `ALLOWED_HOSTS` in `perfume_api/settings.py`.
- The project expects PostgreSQL. Adjust `DATABASES` in settings if you prefer SQLite.

### 4) Migrate and run

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser  # optional but recommended
python manage.py runserver
```

---

## 🔐 Authentication

The project enables the following auth backends (in order):
- SessionAuthentication
- JWT via SimpleJWT
- DRF TokenAuthentication (Bearer)

JWT endpoints:
- `POST /api/token/` — obtain access/refresh tokens
- `POST /api/token/refresh/` — refresh access token
- `POST /api/token/verify/` — verify a token

Use header:
```
Authorization: Bearer <access_or_drf_token>
```

---

## 📦 Data Model (simplified)

- `api.CustomUser` (extends `AbstractUser`)
  - `role`: one of `admin`, `manager`, `customer`
- `api.Category`
  - `gender`: string
- `api.PerfumeDetails`
  - `user` (FK to `CustomUser`, optional)
  - `name`, `description`, `image`, `image2`, `price`, `category` (FK), `in_stock`

Validation highlights:
- `image` must be unique (case-insensitive) and must not contain the word "robot".

---

## 🔗 API Endpoints

Base URLs are registered at the project root. Key routes:

- Item API (ModelViewSet over `PerfumeDetails`)
  - `GET /item_list/` — list
  - `POST /item_list/` — create
  - `GET /item_list/{id}/` — retrieve
  - `PUT /item_list/{id}/` — update
  - `PATCH /item_list/{id}/` — partial update
  - `DELETE /item_list/{id}/` — delete
  - Permissions: read for everyone, write restricted (includes admin-only in viewset)

- Product API (GenericViewSet + mixins over `PerfumeDetails`)
  - `GET /listing/` — list
  - `POST /listing/` — create
  - `GET /listing/{id}/` — retrieve
  - `PUT /listing/{id}/` — update
  - `PATCH /listing/{id}/` — partial update
  - `DELETE /listing/{id}/` — delete

Filtering and search:
- Query params supported: `search`, `ordering`, and exact field filters for `name`, `category`, `price`.
- Examples:
  - `GET /item_list/?search=citrus&ordering=price`
  - `GET /item_list/?name=Acqua&price=120`

Request/response schema (create/update `PerfumeDetails`):
```json
{
  "user": 1,
  "name": "Acqua di Gio",
  "category": 2,
  "price": 120,
  "description": "Citrus aquatic notes",
  "image": "https://example.com/img1.jpg"
}
```

Admin:
- Django admin at `/admin/` (use the superuser you created)

---

## 🗂️ Project Structure

```
.
├── manage.py
├── requirements.txt
├── perfume_api/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── api/
    ├── models.py
    ├── views.py
    ├── serializers.py
    ├── filters.py
    ├── permissions.py
    ├── authentication.py
    └── urls.py
```

---

## 📝 Notes and Caveats

- The router in `api/urls.py` registers a `search` route, but `SearchViewSet` is not defined in the codebase. Remove or implement it to avoid import errors.
- `algoliasearch_django` and `algoliasearch` are referenced in settings for indexing but are not listed in `requirements.txt`. Install them if you enable indexing, or remove them from `INSTALLED_APPS`.
- For production, configure `ALLOWED_HOSTS`, static files, secure settings, and database credentials appropriately.

---

## 🤝 Contributing

Issues and pull requests are welcome.

---

Made with ❤️ using Django + DRF.
