🔐VaultX - Secure Password Manager API

VaultX is a secure password manager backend built with FastAPI and PostgreSQL. It allows users to securely store, manage, and retrieve passwords using JWT authentication and encryption.

Features

- 🔑 User Registration & Login
- 🔒 JWT Authentication
- 🔐 bcrypt Password Hashing
- 🔐 Fernet Password Encryption
- ➕ Add Passwords
- 📋 View Saved Passwords
- ✏️ Update Passwords
- ❌ Delete Passwords
- 🔍 Search Passwords
- ⭐ Mark Favorites
- 📂 Password Categories
- 💪 Password Strength Checker
- 🎲 Secure Password Generator
- 🕒 Created & Updated Timestamps

Tech Stack

- FastAPI
- Python
- PostgreSQL
- SQLAlchemy
- JWT Authentication
- bcrypt
- Cryptography (Fernet)
- Uvicorn

Project Structure

VaultX
│
├── app
│   ├── auth
│   ├── database
│   ├── models
│   ├── routers
│   ├── schemas
│   └── utils
│
├── main.py
├── requirements.txt
├── .env.example
└── README.md

Installation

bash
git clone <repository-url>
cd VaultX

python -m venv venv

.\venv\Scripts\Activate

pip install -r requirements.txt

python -m uvicorn main:app --reload


API Documentation

After starting the server, visit:

http://127.0.0.1:8000/docs


👨‍💻Author
Developed by **Manasa**