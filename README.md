# 📖 SwipeBooks – Backend API

Django REST Framework API powering the SwipeBooks book discovery app.
Serves paginated book data with search, filtering, and author endpoints.
Deployed on Render with Supabase PostgreSQL.

## ⚙️ Tech Stack
- Django 5.x + Django REST Framework
- Supabase PostgreSQL (persistent across Render deploys)
- Knox Token + SimpleJWT Authentication
- django-filter
- Render deployment

## 📡 API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/books/` | Paginated book list (20/page) |
| GET | `/books/?search=orhan` | Search by title/author/ISBN |
| GET | `/books/?isbn=9786...` | Find book by ISBN |
| GET | `/books/?author_id=5` | Filter by author |
| GET | `/books/?ordering=-publish_date` | Sort results |
| GET | `/books/{id}/` | Single book detail |
| GET | `/authors/` | Author list |

## 🗄️ Database
Supabase PostgreSQL managed via Django ORM. Book data imported via
custom management command from CSV. Database state persists across
all Render deploys — no re-import needed after initial setup.

## 🔗 Related
- Mobile App: [SwipeBooks React Native](https://github.com/Busrwa/swipeit)

## 🚀 Getting Started
```bash
git clone https://github.com/Busrwa/SwipeBooksBackend.git
cd SwipeBooksBackend
pip install -r requirements.txt
# Add .env: DATABASE_URL, SECRET_KEY, DEBUG
python manage.py migrate
python manage.py runserver
```
