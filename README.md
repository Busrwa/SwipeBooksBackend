# 📚 SwipeBooks – Backend API

SwipeBooks Backend is a Django REST Framework API built for the SwipeBooks mobile application, a book discovery platform with swipe-based browsing, search, filtering, and author-based exploration.

The backend provides structured book and author data, authentication endpoints, pagination, filtering, ordering, and database persistence through Supabase PostgreSQL. It is designed to support a React Native mobile frontend and is deployable on Render.

## 🚀 Project Overview

SwipeBooks helps users discover books through a mobile-first experience. This backend powers the application by serving book records, author information, search results, and authenticated user operations.

Book data can be imported from a CSV dataset and stored persistently in PostgreSQL.

## ⚙️ Tech Stack

* Python
* Django
* Django REST Framework
* Supabase PostgreSQL
* Knox Token Authentication
* Simple JWT
* django-filter
* Gunicorn
* WhiteNoise
* Render deployment

## ✨ Features

* REST API for book discovery
* Paginated book listing
* Search by title, author, or ISBN
* Filter books by author
* Sort books by ID, title, or publish date
* Author listing and detail endpoints
* Token-based authentication
* PostgreSQL database integration
* Render-ready deployment configuration

## 🔗 API Endpoints

| Method | Endpoint                         | Description                      |
| ------ | -------------------------------- | -------------------------------- |
| GET    | `/books/`                        | Paginated book list              |
| GET    | `/books/?search=orhan`           | Search by title, author, or ISBN |
| GET    | `/books/?isbn=9786...`           | Find book by ISBN                |
| GET    | `/books/?author_id=5`            | Filter books by author           |
| GET    | `/books/?ordering=-publish_date` | Sort book results                |
| GET    | `/books/{id}/`                   | Single book detail               |
| GET    | `/authors/`                      | Author list                      |

## 🗄️ Database

The project uses Supabase PostgreSQL as the production database. Django ORM manages the database models and migrations.

Book records can be imported from CSV data, and the production database persists across Render deployments.

## 🔐 Environment Variables

Create a `.env` file locally based on `.env.example`:

```env
SECRET_KEY=your-django-secret-key
DEBUG=False
DATABASE_URL=postgresql://USER:PASSWORD@HOST:PORT/DATABASE_NAME
ALLOWED_HOSTS=swipebooksbackend.onrender.com,localhost,127.0.0.1
CORS_ALLOWED_ORIGINS=https://swipebooksbackend.onrender.com,http://localhost:19006,http://localhost:8081
```

## 🛠️ Getting Started

```bash
git clone https://github.com/Busrwa/SwipeBooksBackend.git
cd SwipeBooksBackend

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## 🔗 Related Repository

* Mobile App: https://github.com/Busrwa/swipeit

## 📌 Project Type

Django REST API / Mobile App Backend / Book Discovery Platform / Supabase PostgreSQL

## 📄 License

This project is for academic and portfolio purposes.
