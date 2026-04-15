# 🚀 Stage 1 Personal API Deployment (DevOps Project)

![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![Nginx](https://img.shields.io/badge/Nginx-Reverse%20Proxy-green?style=for-the-badge&logo=nginx)
![FastAPI](https://img.shields.io/badge/FastAPI-Python-teal?style=for-the-badge&logo=fastapi)
![Systemd](https://img.shields.io/badge/Systemd-Service-blue?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge)

---

## 👤 Author

**Oluwayemisi Okunrounmu**

GitHub: https://github.com/Yemmmyc  
Email: yemmmyc@hotmail.com  

---

## 📌 Project Overview

This project is a simple production-style API built and deployed on a Linux server using DevOps practices.

It demonstrates:
- API development (FastAPI)
- Reverse proxy (Nginx)
- Process management (Systemd)
- Cloud deployment (Ubuntu VPS)

---

## 🌐 Live URL

http://34.172.253.189/

---

## ⚙️ API Endpoints

| Endpoint | Method | Response |
|----------|--------|----------|
| `/` | GET | {"message": "API is running"} |
| `/health` | GET | {"message": "healthy"} |
| `/me` | GET | {"name": "...", "email": "...", "github": "..."} |

---

## 🏗️ Architecture Diagram

```mermaid
graph TD
A[User Browser] --> B[Nginx Reverse Proxy]
B --> C[Systemd Service]
C --> D[FastAPI App on Uvicorn]
D --> E[JSON Response]
🧱 Infrastructure Stack
Ubuntu Linux Server
FastAPI (Python backend)
Uvicorn ASGI server
Nginx reverse proxy
Systemd service manager
🔐 Deployment Features

✔ Nginx handles public traffic (port 80)
✔ FastAPI runs internally on 127.0.0.1:8000
✔ Systemd ensures auto-restart on reboot
✔ Secure separation of concerns

🚀 How It Works
User sends request to server IP
Nginx receives request
Nginx forwards to FastAPI
FastAPI returns JSON response
Systemd keeps service alive
🎯 Key DevOps Skills Demonstrated
Linux server management
API deployment
Nginx configuration
Systemd service creation
Cloud hosting basics
Production architecture design
📦 Status

✔ Fully deployed
✔ Fully tested
✔ Production-ready


---
