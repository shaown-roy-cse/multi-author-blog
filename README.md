# Multi Author Blog Platform

A Django-based multi-author blogging platform where users can register, login, create posts, comment, like posts, and manage author profiles.

## Features

### User Authentication & Roles
- User registration and login system
- Secure password handling using Django authentication
- Users are Readers by default
- Admin can promote users to Authors
- Authors can create and manage their own posts

### Blog Features
- Create, update and delete posts
- Draft and Published post system
- Featured image upload
- Automatic slug generation
- View count analytics

### Category & Tag Management
- Category management system
- Many-to-many Tag system
- Admin can manage categories and tags

### Interaction Features
- Comment system
- Like and unlike system
- Users cannot like the same post multiple times

### Search & Navigation
- Search posts by title and content
- Filter posts by category and tag
- Pagination support

### Admin Panel
- Manage users
- Manage authors
- Manage posts
- Manage categories, tags and comments


# Installation and Setup

## 1. Clone Repository

```bash
git clone https://github.com/shaown-roy-cse/multi-author-blog.git
```

Go to project directory:

```bash
cd multi-author-blog
```


## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```


## 3. Install Requirements

```bash
pip install -r requirements.txt
```


## 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

A sample environment file is provided:

```
.env.example
```


## 5. Run Migrations

```bash
python manage.py migrate
```


## 6. Create Superuser

```bash
python manage.py createsuperuser
```


## 7. Run Server

```bash
python manage.py runserver
```

Open in browser:

```
http://127.0.0.1:8000/
```


## Technologies Used

- Python 3
- Django
- SQLite Database
- HTML
- Bootstrap
- Git & GitHub


## Media Files

The project supports featured image upload using Django MEDIA_ROOT and MEDIA_URL configuration.


## Project Repository

GitHub:

https://github.com/shaown-roy-cse/multi-author-blog
