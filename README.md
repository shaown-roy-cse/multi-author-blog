# Multi Author Blog Platform

A Django-based multi-author blogging platform where users can register, login, create posts, comment, like posts, and manage author profiles.

## Features

- User Registration and Login
- Author Profile Management
- Create, Update and Delete Posts
- Comment System
- Like System
- Category and Tag Management
- Author Dashboard

## Installation and Setup

### 1. Clone Repository

git clone repository_url

### 2. Create Virtual Environment

python -m venv venv

Activate:

Windows:
venv\Scripts\activate

### 3. Install Requirements

pip install -r requirements.txt

### 4. Configure Environment Variables

Create a `.env` file:

SECRET_KEY=your_secret_key
DEBUG=True

### 5. Run Migrations

python manage.py migrate

### 6. Create Superuser

python manage.py createsuperuser

### 7. Run Server

python manage.py runserver

Open:

http://127.0.0.1:8000/