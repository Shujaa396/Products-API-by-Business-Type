# 🧾 Invoice API & Core Backend Enhancements – Nexus Desktop POS

A comprehensive backend task focused on **API validation, authentication, invoice processing, offline sync handling**, and **robust testing** using **FastAPI** and **PostgreSQL** for the Nexus Desktop POS system.

---

## 🛠️ Tech Stack
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![JWT](https://img.shields.io/badge/Auth-JWT-orange?style=for-the-badge&logo=jsonwebtokens)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black)
![Oracle](https://img.shields.io/badge/Oracle_Cloud-Free_VM-red?style=for-the-badge&logo=oracle)

---

## 📖 Task Overview
This task covers **core backend improvements** completed within one week, including API validation, authentication utilities, invoice creation logic, offline sync handling, and extensive API testing using Postman and Swagger.

---

## ✅ Completed Tasks

### 🔹 FastAPI Ping Endpoint
- Implemented `GET /ping` to verify server health.
- Tested using Postman and browser.
- Response: `{ "message": "pong" }`

---

### 🔹 Password Hashing & Authentication
- Implemented `security.py` using **passlib**.
- Functions:
  - `get_password_hash()`
  - `verify_password()`
- Configured bcrypt hashing.
- Integrated with FastAPI authentication flow.

---

### 🔹 Invoice API – POST `/invoice/create`
Implemented and finalized invoice creation with strict validation.

#### Validations Added:
- Tax range: **0–20%**
- Quantity must be **> 0**
- Items must exist in stock
- User authorization via token

---

### 🔹 Invoice Schema
```text
invoice_id
user_id
items
amount
tax
total
status
synced_at
is_offline
```

---

### 🔹 Offline Sync Logic
- API accepts **batch of buffered invoices**
- Stores invoices with timestamps
- Ensures consistency during offline → online sync

---

## 📦 Deliverables
- Updated SQLAlchemy models
- Custom validation error responses (422)
- Postman test collection
- 3 sample inputs (valid + invalid)
- Demo endpoint tested locally / VM deployment

---

## 🧪 Testing & Verification

| Test Case | Result |
|----------|--------|
| Postman full payload | ✅ |
| Postman partial payload | ✅ |
| Invalid tax / quantity | ✅ 422 |
| Unauthorized request | ✅ 401 |
| Offline invoice batch (5+) | ✅ |
| Swagger models & examples | ✅ |
| DB schema verification | ✅ |

---

## 🧠 Methodology
1. Designed schema updates for invoices.
2. Implemented validation logic using Pydantic.
3. Added offline batch handling logic.
4. Secured routes using JWT.
5. Tested endpoints via Postman & Swagger.
6. Verified database entries via PgAdmin / psql.

---

## 📁 Folder Structure
```
app/
├── routes/
│   └── invoice.py
├── models/
│   └── invoice.py
├── schemas/
│   └── invoice.py
├── auth/
│   └── security.py
├── database/
│   └── connection.py
├── main.py
└── README.md
```

---

## 👤 Author
**Syed Shujaa Hussain**  
Backend Developer  

[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:web.shujaa10@gmail.com)  
[![GitHub](https://img.shields.io/badge/GitHub-000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Shujaa396)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/syed-shujaa-hussain-69113b289)

