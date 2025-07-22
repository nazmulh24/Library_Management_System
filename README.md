# Library Management System - REST API

A comprehensive RESTful Library Management System built using Django REST Framework (DRF). It provides endpoints for managing books, authors, categories, users, and book circulation with automated fine calculations. The project implements JWT authentication using Djoser and includes comprehensive API documentation with Swagger.

## Features
- **Book Management** - Complete CRUD operations with advanced filtering and search
- **Author & Category Management** - Manage author profiles and book categories
- **User Management** - JWT-based authentication with role-based permissions (Librarians vs Members)
- **Book Circulation System** - Borrow and return books with automated fine calculations
- **Popular & Available Books** - Custom endpoints for most borrowed and available books
- **Email Integration** - User activation and password reset functionality
- **API Documentation** - Interactive Swagger and ReDoc documentation

## Technologies Used
- **Django 5.2.4** - Backend framework
- **Django REST Framework (DRF) 3.16.0** - API development
- **Djoser 2.3.3** - Authentication system
- **Simple JWT 5.5.0** - JWT authentication
- **drf-yasg 1.21.10** - API documentation (Swagger)
- **django-filter 25.1** - Advanced filtering capabilities
- **Pillow 11.3.0** - Image processing for book covers and author photos
- **SQLite** (development) / **PostgreSQL** (production ready) - Database

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/nazmulh24/Library_Management_System.git
   cd Library_Management_System
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data (Optional):**
   ```bash
   python manage.py loaddata fixtures/catalog_data.json
   ```

7. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

## API Documentation
Swagger documentation is available at:
```
http://127.0.0.1:8000/swagger/
```

ReDoc documentation is available at:
```
http://127.0.0.1:8000/redoc/
```

## API Endpoints

### Authentication Endpoints
- `POST /auth/users/` - User registration
- `POST /auth/users/activation/` - Account activation
- `POST /auth/jwt/create/` - Login (get JWT token)
- `POST /auth/jwt/refresh/` - Refresh JWT token
- `POST /auth/users/reset_password/` - Password reset request
- `GET /auth/users/me/` - Current user profile

### Catalog Endpoints
- `GET /api/v1/authors/` - List all authors
- `POST /api/v1/authors/` - Create new author (librarian only)
- `GET /api/v1/categories/` - List all categories
- `POST /api/v1/categories/` - Create new category (librarian only)
- `GET /api/v1/books/` - List all books (with filtering & search)
- `POST /api/v1/books/` - Create new book (librarian only)
- `GET /api/v1/books/popular/` - Get top 10 most borrowed books
- `GET /api/v1/books/available/` - Get books with available copies

### Circulation Endpoints
- `GET /api/v1/borrow-records/` - List borrow records (filtered by user role)
- `POST /api/v1/borrow-records/` - Create new borrow record
- `POST /api/v1/borrow-records/{id}/return/` - Return a borrowed book

## Environment Variables
Create a `.env` file in the root directory and add the following:
```ini
#--> Email Configuration
EMAIL_HOST=smtp.gmail.com
EMAIL_USE_TLS=True
EMAIL_PORT=587
EMAIL_HOST_USER=snazmulhossains24@gmail.com
EMAIL_HOST_PASSWORD=your-app-password

DEFAULT_FROM_EMAIL=snazmulhossains24@gmail.com
ADMIN_EMAIL=snazmulhossains24@gmail.com

#--> Database Configuration (Production)
# user=your_postgres_user
# password=your_postgres_password
# host=your_host
# port=5432
# dbname=your_database_name

#--> Cloudinary Configuration (Optional for media files)
# cloud_name=your_cloud_name
# api_key=your_api_key
# api_secret=your_api_secret
```

## User Roles & Permissions

### Librarian (Staff Users)
- Full CRUD access to all books, authors, and categories
- Can view all borrow records
- Access to admin panel
- Can manage user accounts

### Member (Regular Users)
- Read-only access to books, authors, and categories
- Can borrow and return books
- Can only view their own borrow records
- Can update their profile information

## Advanced Features

### Search & Filtering
```bash
# Search books by title, subtitle, or ISBN
GET /api/v1/books/?search=python

# Filter by category or author
GET /api/v1/books/?category=programming&author=john

# Filter available books only
GET /api/v1/books/?available_copies__gt=0

# Order results
GET /api/v1/books/?ordering=-created_at
```

### JWT Authentication
Include JWT token in request headers:
```
Authorization: JWT your_access_token_here
```

## Project Structure
```
Library-Management-Project/
├── api/                    # API configuration and routing
├── catalog/                # Books, Authors, Categories models and views
├── circulation/            # Borrowing system and permissions
├── users/                  # Custom user model and authentication
├── fixtures/               # Sample data
├── media/                  # Uploaded files (photos, book covers)
├── library_management/     # Project settings and configuration
├── manage.py
├── requirements.txt
└── .env                    # Environment variables
```

## License
This project is licensed under the MIT License.

---
### Author
[Nazmul Hossain](https://github.com/nazmulh24)
