PETLYNK – PREMIUM PET DATING & BONDING PLATFORM
==============================================

TEAM DETAILS
------------

Team Name:
VOIDIX

Team Leader:
Sajeer F M

Team Members:
Patrick Davis Jerry


APPLICATION OVERVIEW
-------------------

PetLynk is a full-stack web-based animal social matchmaking and bonding platform designed to connect pets through intelligent, preference-based compatibility matching. The system enables users to create rich pet profiles, define lifestyle and behavioral attributes, and discover suitable companions using a structured recommendation approach.

Unlike traditional social platforms, PetLynk focuses on pet-centric characteristics such as energy level, personality, habitat, diet style, and favorite activities to generate meaningful matches.

The platform supports secure authentication, profile management, bonding requests, and real-time one-to-one messaging between mutually matched pets. A compatibility percentage is calculated to help users quickly evaluate potential matches.

PetLynk demonstrates the practical implementation of a matchmaking system integrated with communication features and serves as a comprehensive example of a real-world social networking application.


IMPLEMENTED FEATURES
-------------------

1. User Authentication & Security
   - User registration and login
   - Session-based authentication
   - Secure logout
   - Access control for protected pages

2. Pet Profile Management
   - Create and edit pet profiles
   - Upload profile picture
   - Store pet details:
     Name
     Species
     Age
     Gender
     Energy level
     Social style
     Habitat preference
     Home territory
     Personality traits
     Diet style
     Favorite activity

3. Preference-Based Matchmaking
   - Intelligent matching using lifestyle and behavior attributes
   - Automatic compatibility score generation
   - Suggested matches displayed in card format

4. Bond Request System
   - Send bond requests
   - Visual confirmation of sent requests
   - Mutual bonding required before chat

5. Real-Time Messaging
   - One-to-one private chat
   - Chat unlocked after mutual bonding
   - Message timestamps
   - Online/active status indicator

6. Match Dashboard
   - View all recommended matches
   - View compatibility percentage
   - Quick bond button

7. Cloud Deployment (AWS)
   - Hosted on Amazon Web Services EC2
   - Centralized cloud database
   - Scalable and reliable infrastructure

8. User-Friendly Interface
   - Clean and responsive design
   - Mobile-friendly layout
   - Simple navigation

9. System Performance & Reliability
   - Fast page loading
   - Organized database structure
   - Scalable backend architecture


TECHNOLOGY STACK
----------------

Frontend:
- HTML5
- CSS3
- JavaScript

Backend:
- Python
- Django Framework

Database:
- SQLite (Development)

Server & Deployment:
- AWS EC2
- Nginx
- Gunicorn
- Ubuntu Linux


SETUP AND EXECUTION INSTRUCTIONS
--------------------------------

1. Clone the repository
   git clone <repository_url>

2. Create virtual environment
   python -m venv venv
   source venv/bin/activate

3. Install dependencies
   pip install -r requirements.txt

4. Apply database migrations
   python manage.py makemigrations
   python manage.py migrate

5. Create admin user
   python manage.py createsuperuser

6. Run development server
   python manage.py runserver

7. Access application
   http://petlynk.webs.vc


ASSUMPTIONS, LIMITATIONS & KNOWN ISSUES
---------------------------------------

- Internet connection required
- SQLite suitable only for development
- Limited scalability on free hosting tier
- No push notifications in current version


DEMO VIDEO LINK
---------------

https://www.youtube.com/watch?v=d7tD3VNhC4w


==============================================
END OF FILE
==============================================
