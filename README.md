
# Authentication System – Django REST Framework

A secure authentication system using Django REST Framework with email-based OTP verification, JWT authentication, OTP expiration (10 minutes), throttling, and SQL injection prevention.

## 🚀 Features

- ✅ Register with email + profile (with OTP verification)
- ✅ Email OTP (expires in 10 minutes)
- ✅ OTP verification endpoint
- ✅ Resend OTP endpoint (rate-limited)
- ✅ JWT login & logout
- ✅ Throttling for sensitive endpoints
- ✅ SQL injection prevention via validation

---

## 🚀 Getting Started

### ✅ 1. Clone the Repository

```bash
git clone https://github.com/MatthewOhimai/django-authentication.git
cd django-authentication
```

---

### ✅ 2. Create and Activate a Virtual Environment

#### For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

#### For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### ✅ 3. Install Dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

---

### ✅ 4. Set Up Environment Variables

Create a `.env` file in the project root with:

```env
SECRET_KEY=your-django-secret-key
DEBUG=True
```

---

### ✅ 5. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### ✅ 6. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🔐 Authentication Endpoints

All routes are under the **users** app.

| Method | Endpoint     | Description               | Auth Required | Status     |
|--------|--------------|---------------------------|---------------|------------|
| POST   | `/register/` | Register a new user       | ❌            | ✅ Working |
| POST   | `/login/`    | Login and get JWT tokens  | ❌            | ✅ Working |
| GET    | `/me/`       | Get current user profile  | ✅ (Bearer)    | ✅ Working |

---


## 📦 Endpoints & Postman Guide

### ✅ 1. Register

`POST /register/`

```json
{
  "username": "john",
  "email": "john@gmail.com",
  "password": "john1234",
  "profile": {
    "phone_number": "08012345678",
    "role": "student",
    "date_of_birth": "2001-10-10"
  }
}
```

### 🔐 2. Verify OTP

`POST /verify-email/`

```json
{
  "email": "john@gmail.com",
  "otp": "123456"
}
```

### 🔁 3. Resend OTP

`POST /resend-otp/`

```json
{
  "email": "john@gmail.com"
}
```

### 🔑 4. Login

`POST /login/`

```json
{
    "email": "matthew@gmail.com",
    "password": "secure1234"
}
```

### 👤 5. Get Authenticated User

**GET** `/me/`  
**Headers:**
```http
Authorization: Bearer your-access-token
```

**Response:**
```json
{
  "id": 1,
  "username": "john",
  "email": "john@gmail.com",
  "profile": {
    "phone_number": "08012345678",
    "role": "student",
    "date_of_birth": "2001-10-10"
  }
}
```

### 🚪 6. Logout

`POST /logout/`

Header: `Authorization: Bearer <access_token>`

### ✅ Response:

```json
{
    "detail": "Logged out successfully"
}
```

---

## 🛡️ Throttling Rules

- OTP verification & resend are throttled (3/min).
- Uses `AnonRateThrottle` and `UserRateThrottle`.

## ⚙️ Technologies

- Django, Django REST Framework
- PostgreSQL/MySQL
- pyotp for OTP generation
- djangorestframework-simplejwt for JWT

## 📁 Folder Structure

- `models.py` – Custom user & profile models
- `serializers.py` – User, profile, and OTP serializers
- `views.py` – All endpoint views
- `utils.py` – For email sending (You can edit the email settings to smtp for production)
- `urls.py` – Endpoint routing

---


## 🧪 Test with Postman

1. Register – Copy OTP from console/email.
2. Verify OTP – Must be within 10 minutes.
3. Login – After verification only.
4. Logout – Provide refresh token.
5. Resend OTP – Rate-limited to 3/min.

---


## 📁 Project Structure

```
DJANGO-AUTHENTICATION/
│
├── django_authentication/          # Project configuration
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── accounts/            # Authentication app
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── .env              # Environment secrets
├── .gitignore
├── db.sqlite3
├── manage.py
├── requirements.txt
└── venv/
```

---

## ✍️ Author

- **Matthew Ohimai**
- GitHub: [@MatthewOhimai](https://github.com/MatthewOhimai)
- X (Twitter): [@MatthewOhimai](https://x.com/MatthewOhimai)
- LinkedIn: [@MatthewOhimai](https://www.linkedin.com/in/matthew-ohimai)
