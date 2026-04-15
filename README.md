# 🚀 Stage 1 Personal API Deployment (DevOps Project)

---

## 👤 Author

**Oluwayemisi Okunrounmu**

- GitHub: https://github.com/Yemmmyc  
- Email: yemmmyc@hotmail.com  

---

## 📌 Project Overview

This project is a production-style REST API deployed on a Linux VPS using DevOps practices.

It demonstrates:

- FastAPI backend development  
- Nginx reverse proxy  
- Systemd service management  
- Cloud deployment (Ubuntu VPS)  

---

## 🌐 Live URL

http://34.172.253.189/

---

## ⚙️ API Endpoints

| Endpoint | Method | Response |
|----------|--------|----------|
| `/` | GET | `{ "message": "API is running" }` |
| `/health` | GET | `{ "message": "healthy" }` |
| `/me` | GET | `{ "name": "Oluwayemisi Okunrounmu", "email": "yemmmyc@hotmail.com", "github": "https://github.com/Yemmmyc" }` |

---

## 🏗️ Architecture Diagram

![Architecture](https://raw.githubusercontent.com/Yemmmyc/stage-1-api/main/architecture.png)

---

## 🧱 System Architecture Flow

```mermaid
graph TD
A[User Browser] --> B[Nginx Reverse Proxy]
B --> C[Systemd Service]
C --> D[FastAPI App (Uvicorn)]
D --> E[JSON Response]

🧱 Infrastructure Stack
Ubuntu Linux Server
FastAPI (Python backend)
Uvicorn ASGI server
Nginx reverse proxy
Systemd service manager

🔐 Deployment Features
Nginx handles public traffic (port 80 / 443)
FastAPI runs internally on 127.0.0.1:8000
Systemd ensures auto-restart on reboot
Secure separation of concerns

🚀 How It Works
User sends request to server IP
Nginx receives request
Nginx forwards to FastAPI
FastAPI returns JSON response
Systemd keeps service alive

🎯 DevOps Skills Demonstrated
Linux server management
API deployment
Nginx configuration
Systemd service creation
Cloud hosting (VPS)
Production architecture design

📦 Status

✔ Fully deployed
✔ Fully tested
✔ Production-ready
