# 🐾 PetLynk – Premium Pet Dating & Bonding Platform

PetLynk is a full-stack, web-based animal social matchmaking and bonding platform designed to connect pets through intelligent, preference-based compatibility matching. 

**🎥 Live Demo:** [Watch the PetLynk Demo on YouTube](https://youtu.be/QOVgIyTfecI)

---

## 📑 Table of Contents
- [Application Overview](#-application-overview)
- [Key Features](#-key-features)
- [Technology Stack](#-technology-stack)
- [Setup and Execution](#-setup-and-execution)
- [Team Details](#-team-details)

---

## 📖 Application Overview

Unlike traditional social platforms, PetLynk focuses on pet-centric characteristics such as energy level, personality, habitat, diet style, and favorite activities to generate meaningful matches. The system enables users to create rich pet profiles, define lifestyle and behavioral attributes, and discover suitable companions using a structured recommendation approach.

The platform supports secure authentication, profile management, bonding requests, and real-time one-to-one messaging between mutually matched pets. A compatibility percentage is calculated to help users quickly evaluate potential matches. 

*PetLynk demonstrates the practical implementation of a matchmaking system integrated with communication features and serves as a comprehensive example of a real-world social networking application.*

---

## ✨ Key Features

### 🔐 1. User Authentication & Security
- User registration and login.
- Session-based authentication.
- Secure logout and access control for protected pages.

### 🐶 2. Pet Profile Management
- Create and edit comprehensive pet profiles.
- Upload profile pictures.
- Store specific pet details: *Name, Species, Age, Gender, Energy level, Social style, Habitat preference, Home territory, Personality traits, Diet style, and Favorite activity.*

### 🎯 3. Preference-Based Matchmaking
- Intelligent matching using lifestyle and behavior attributes.
- Automatic compatibility score generation.
- Suggested matches elegantly displayed in a card format.

### 🤝 4. Bond Request System
- Send and receive bond requests.
- Visual confirmation of sent requests.
- Mutual bonding required before chat access is granted.

### 💬 5. Real-Time Messaging
- One-to-one private chat (unlocked after mutual bonding).
- Message timestamps and online/active status indicators.
- Auto-refresh capabilities for seamless conversation.

### 📊 6. Match Dashboard
- View all recommended matches in one place.
- Instantly view compatibility percentages.
- Quick "Bond" action button.

### ☁️ 7. Cloud Deployment
- Hosted securely on Amazon Web Services (AWS) EC2.
- Centralized cloud database.
- Scalable and reliable infrastructure.

### 📱 8. User-Friendly Interface
- Clean, responsive, and mobile-friendly design.
- Simple and intuitive navigation.

---

## 🛠 Technology Stack

**Frontend:**
- HTML5
- CSS3
- JavaScript

**Backend:**
- Python
- Django Framework

**Database:**
- SQLite (Development)

**Server & Deployment:**
- AWS EC2
- Nginx
- Gunicorn
- Ubuntu Linux

---

## 🚀 Setup and Execution

Follow these steps to get the project running on your local machine:

**1. Clone the repository**
```bash
git clone <repository_url>
cd <repository_directory>
```

**2. Create and activate a virtual environment**
*For macOS/Linux:*
```bash
python3 -m venv venv
source venv/bin/activate
```
*For Windows:*
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Apply database migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

**5. Create a superuser (Admin)**
```bash
python manage.py createsuperuser
```

**6. Run the development server**
```bash
python manage.py runserver
```

**7. Access the application**
Open your web browser and navigate to: `http://localhost:8000/`

---

## 👥 Team Details

**Team Name:** VOIDIX

| Role | Name |
| :--- | :--- |
| **Team Leader** | Sajeer F M |
| **Team Member** | Patrick Davis Jerry |

---
