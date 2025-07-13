
# 🛍️ Django REST Framework Commerce API

Welcome to the **Commerce API**, a powerful and secure backend service for an e-commerce application built with **Django REST Framework**, using **PostgreSQL**, JWT and Session authentication, and role-based access.

---

## 🎯 Overview

This project is designed to serve as the backend for a commercial website. It includes:

- 🔐 JWT + Session authentication
- 🧑‍🤝‍🧑 User roles: **Customer**, **Staff**, **Admin**
- 🌐 CORS handling for frontend integration
- 🐘 PostgreSQL as the primary database
- 📦 All dependencies in `requirements.txt`
- 🛡️ `.env` for all sensitive configurations

---

## ⚙️ Installation Guide

### 1. Clone the repository

```bash
git clone https://github.com/gkvartskhava/perfumeBack
cd commerce-api
```

### 2. Set up a virtual environment

#### On Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

#### On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root

```dotenv
SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### 5. Run migrations and start the server

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

---

## 🔐 Authentication

This API supports:

- ✅ **JWT Authentication**
- ✅ **Session Authentication**

Use `/api/token/` to obtain JWTs and `/api/token/refresh/` to refresh them.

---

## 👥 Roles & Permissions

- **Customer**: Can browse products and manage their orders.
- **Staff**: Can manage inventory and access customer order data.
- **Admin**: Full access, including user and permission management.

---

## 🔗 Sample API Endpoints

| Endpoint                | Method | Description                  | Auth Required |
|-------------------------|--------|------------------------------|---------------|
| `/api/token/`           | POST   | Get JWT token                | ❌            |
| `/api/token/refresh/`   | POST   | Refresh JWT token            | ❌            |
| `/api/products/`        | GET    | List products                | ❌            |
| `/admin/`               | GET    | Django admin panel           | ✅ (Admin)    |

---

## 🌍 CORS Configuration

CORS is managed via `django-cors-headers`.

Example config in `settings.py`:
```python
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Your frontend app URL
]
```

---

## 📁 Project Structure

```
📦 commerce_api/
├── app/
├── manage.py
├── requirements.txt
├── .env
└── README.md
```

---

## 👨‍💻 Contributing

Found a bug or want to contribute?  
Feel free to open an issue or submit a pull request. Contributions are welcome! ❤️

---

Made with ❤️ using Django + DRF
