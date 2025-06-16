# GROUP_PROJECT_DJANGO_REST_API

This project is a **Django REST Framework (DRF)**-based API built collaboratively as a group project. It provides RESTful endpoints for managing and accessing data in a scalable and secure manner. 

## Description:
The project is a product review project which enables a user to either review, market or list reviews. 

---

## Goal

The goal of this project is to empower a user with the knowledge of which product, e.g mobile, to buy for a specific purpose or need.

---

## 🚀 Features

- Built with Django and Django REST Framework
- Modular and scalable project structure
- Token-based authentication 
- CRUD operations for core resources
- Pagination, filtering, and search support 
- Swagger or ReDoc API documentation
- PostgreSQL or SQLite database support 

---

## 🛠 Tech Stack

- **Backend**: Django, Django REST Framework
- **Database**: PostgreSQL / SQLite (set as needed at the settings.py)
- **Authentication**: DRF TokenAuthentication 
- **Documentation**: Swagger / ReDoc (via `drf-yasg`)

---

## 📁 Project Structure

GROUP_PROJECT_DJANGO_REST_API/django_project_root/

├── django_project/ # Django project settings

├── app_name/ # Core Django apps: accounts, contacts, marketers, mobiles

│ ├── models.py

│ ├── serializers.py

│ ├── views.py

│ ├── urls.py

│ └── tests.py

├── manage.py

├── requirements.txt

└── README.md


---

---

## ⚙️ Setup Instructions

### 🔐 Prerequisites

- Python 3.8+
- pip
- (Optional) PostgreSQL and `psycopg2` if using Postgres

### 🧪 Installation

```bash
# Clone the repo
git clone https://github.com/mrt0090/GROUP_PROJECT_DJANGO_REST_API.git
cd  django_project_root

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

## Test Authentication Endpoints

Now you can test the following API endpoints:

User Login: POST /api/accounts/users/login/
```json

{
  "username": "testuser",
  "password": "password123"
}
```
+ User Logout: POST /api/accounts/users/logout/
+ User Registration: POST /api/accounts/users/registration/
```json

{
  "username": "testuser",
  "password1": "password123",
  "password2": "password123"
}
```
+ Password Reset: POST /api/accounts/users/password/reset/
+ Token Authentication (if needed):
```sh

curl -X POST -H "Content-Type: application/json" -d '{"username":"testuser", "password":"password123"}' http://127.0.0.1:8000/api/accounts/users/login/
```
📄 API Documentation
Swagger UI: http://localhost:8000/swagger/

ReDoc: http://localhost:8000/redoc/

Generated using drf-yasg 

✅ Running Tests

```
python manage.py test
```
👥 Contributors
+ Nkemdilim Julie Chime
+ Taras Bilan




📝 License
This project is licensed under the MIT License. 

### Run this code according to the assigned Database (as of now)

At settings.py, if database is set to sqlite3, run this way: goto Terminal, make sure you are at the manage.py folder level, source .venv/bin/activate, then --->
```
python manage.py runserver 8080
```
if not, run this way:
```
docker-compose up --build
```
