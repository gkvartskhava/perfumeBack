
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

// 2. Set up a virtual environment

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate



// 3. Install required packages 

pip install -r requirements.txt

// 4. Create a .env file in the root
dotenv

SECRET_KEY=your_secret_key
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432


// 5. Run migrations and start server
bash

python manage.py makemigrations
python manage.py migrate
python manage.py runserver