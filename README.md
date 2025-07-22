# 📚 Library Management System - Professional REST API

[![Django](https://img.shields.io/badge/Django-5.2.4-green.svg)](https://djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django%20REST%20Framework-3.16.0-red.svg)](https://www.django-rest-framework.org/)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue.svg)](https://postgresql.org/)
[![Deployment](https://img.shields.io/badge/Deployed%20on-Vercel-black.svg)](https://vercel.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> A comprehensive, production-ready RESTful Library Management System built with Django REST Framework, featuring JWT authentication, role-based permissions, automated fine calculations, and cloud-based media storage. Successfully deployed on Vercel with PostgreSQL and Cloudinary integration.

## ✨ Key Features

### 🔐 **Authentication & Security**
- **JWT Authentication** using Djoser with refresh token support
- **Role-based Access Control** (Librarians vs Members)
- **Email Verification** for account activation
- **Password Reset** functionality via email
- **CSRF Protection** and secure headers

### 📖 **Core Library Management**
- **Book Management** - Complete CRUD with advanced filtering, search, and pagination
- **Author Management** - Biographical data with photo uploads via Cloudinary
- **Category Management** - Organized book categorization system
- **Circulation System** - Automated borrowing/returning with due date tracking
- **Fine Management** - Automated calculation and tracking of overdue penalties

### 🚀 **Advanced Features**
- **Smart Search** - Multi-field search across titles, subtitles, and ISBN
- **Advanced Filtering** - By category, author, publication year, availability
- **Popular Books API** - Top 10 most borrowed books analytics
- **Real-time Availability** - Live book availability tracking
- **Email Integration** - SMTP configuration for notifications
- **Cloud Storage** - Cloudinary integration for media files

### 📊 **API & Documentation**
- **Interactive API Documentation** - Swagger UI and ReDoc
- **RESTful Design** - Clean, intuitive API endpoints
- **Comprehensive Serialization** - Detailed request/response formats
- **Error Handling** - Proper HTTP status codes and error messages

## 🛠️ Technology Stack

### **Backend Core**
- **Django 5.2.4** - Robust Python web framework
- **Django REST Framework 3.16.0** - Powerful API development
- **PostgreSQL** - Production database (Supabase hosted)
- **Python 3.11+** - Modern Python features

### **Authentication & Security**
- **Djoser 2.3.3** - Advanced authentication system
- **Simple JWT 5.5.0** - JSON Web Token implementation
- **WhiteNoise** - Efficient static file serving

### **API Documentation**
- **drf-yasg 1.21.10** - OpenAPI/Swagger documentation
- **Interactive UI** - Swagger and ReDoc interfaces

### **Database & Storage**
- **PostgreSQL** - Reliable relational database
- **Cloudinary** - Cloud-based media storage and optimization
- **django-filter 25.1** - Advanced filtering capabilities

### **Deployment & Production**
- **Vercel** - Serverless deployment platform
- **WhiteNoise** - Static file serving
- **Environment Variables** - Secure configuration management

## 🚀 Live Demo

**🌐 Live API:** [https://your-vercel-url.vercel.app](https://your-vercel-url.vercel.app)

**📚 API Documentation:**
- Swagger UI: [https://your-vercel-url.vercel.app/swagger/](https://your-vercel-url.vercel.app/swagger/)
- ReDoc: [https://your-vercel-url.vercel.app/redoc/](https://your-vercel-url.vercel.app/redoc/)

## 📋 API Endpoints Overview

### 🔐 **Authentication**
```http
POST   /auth/users/                    # User registration
POST   /auth/users/activation/         # Account activation
POST   /auth/jwt/create/              # Login (JWT token)
POST   /auth/jwt/refresh/             # Refresh token
POST   /auth/users/reset_password/    # Password reset
GET    /auth/users/me/               # Current user profile
```

### 📚 **Library Catalog**
```http
# Authors
GET    /api/v1/authors/              # List authors (paginated)
POST   /api/v1/authors/              # Create author (librarian)
GET    /api/v1/authors/{id}/         # Author details
PUT    /api/v1/authors/{id}/         # Update author (librarian)
DELETE /api/v1/authors/{id}/         # Delete author (librarian)

# Categories
GET    /api/v1/categories/           # List categories
POST   /api/v1/categories/           # Create category (librarian)
GET    /api/v1/categories/{id}/      # Category details
PUT    /api/v1/categories/{id}/      # Update category (librarian)
DELETE /api/v1/categories/{id}/      # Delete category (librarian)

# Books
GET    /api/v1/books/                # List books (filtered, searched, paginated)
POST   /api/v1/books/                # Create book (librarian)
GET    /api/v1/books/{id}/           # Book details
PUT    /api/v1/books/{id}/           # Update book (librarian)
DELETE /api/v1/books/{id}/           # Delete book (librarian)
GET    /api/v1/books/popular/        # Top 10 borrowed books
GET    /api/v1/books/available/      # Available books only
```

### 🔄 **Circulation Management**
```http
GET    /api/v1/borrow-records/       # List borrow records (role-filtered)
POST   /api/v1/borrow-records/       # Create borrow record
GET    /api/v1/borrow-records/{id}/  # Borrow record details
PUT    /api/v1/borrow-records/{id}/  # Update borrow record
DELETE /api/v1/borrow-records/{id}/  # Delete borrow record
POST   /api/v1/borrow-records/{id}/return/  # Return book (with fine calculation)
```

## ⚡ Quick Start Guide

### Prerequisites
- **Python 3.11+**
- **pip** package manager
- **Git** for version control
- **PostgreSQL** (optional for local development)

### 🔧 Local Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/nazmulh24/Library_Management_System.git
   cd Library_Management_System
   ```

2. **Set up Virtual Environment**
   ```bash
   python -m venv library_env
   source library_env/bin/activate  # On Windows: library_env\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   Create a `.env` file in the project root:
   ```env
   # Email Configuration (Gmail SMTP)
   EMAIL_HOST=smtp.gmail.com
   EMAIL_USE_TLS=True
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-specific-password
   DEFAULT_FROM_EMAIL=your-email@gmail.com
   ADMIN_EMAIL=admin@yourlibrary.com

   # Database Configuration (Production)
   user=your_postgres_user
   password=your_secure_password
   host=your_database_host
   port=5432
   dbname=library_management_db

   # Cloudinary Configuration (Media Storage)
   cloud_name=your_cloudinary_name
   api_key=your_cloudinary_key
   api_secret=your_cloudinary_secret
   CLOUDINARY_URL=cloudinary://api_key:api_secret@cloud_name
   ```

5. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

6. **Create Superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Load Sample Data (Optional)**
   ```bash
   python manage.py loaddata fixtures/catalog_data.json
   ```

8. **Start Development Server**
   ```bash
   python manage.py runserver
   ```

   Access the application:
   - **API Root:** http://127.0.0.1:8000/
   - **Admin Panel:** http://127.0.0.1:8000/admin/
   - **Swagger Documentation:** http://127.0.0.1:8000/swagger/
   - **ReDoc Documentation:** http://127.0.0.1:8000/redoc/

## 🔐 Authentication Guide

### JWT Token Usage
```http
# Get Access Token
POST /auth/jwt/create/
{
    "email": "user@example.com",
    "password": "securepassword123"
}

# Include token in requests
Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9...
```

### User Roles & Permissions

#### 👨‍💼 **Librarian (Staff Users)**
- ✅ Full CRUD access to books, authors, categories
- ✅ View all borrow records and user data
- ✅ Access to Django admin panel
- ✅ User account management capabilities
- ✅ Fine management and reporting

#### 👤 **Member (Regular Users)**  
- ✅ Read-only access to catalog (books, authors, categories)
- ✅ Borrow and return books
- ✅ View personal borrow history and fines
- ✅ Update personal profile information
- ❌ No administrative privileges

## 🔍 Advanced API Features

### Smart Search & Filtering
```bash
# Multi-field search
GET /api/v1/books/?search=django python programming

# Category filtering
GET /api/v1/books/?category=programming&author__first_name=john

# Availability filtering
GET /api/v1/books/?available_copies__gt=0

# Combined filtering with ordering
GET /api/v1/books/?category=science&ordering=-created_at&page=2

# Date range filtering
GET /api/v1/borrow-records/?borrow_date__gte=2024-01-01&borrow_date__lte=2024-12-31
```

### Custom Analytics Endpoints
```bash
# Most popular books
GET /api/v1/books/popular/

# Currently available books  
GET /api/v1/books/available/

# Overdue books (with fine calculations)
GET /api/v1/borrow-records/?is_returned=false&due_date__lt=today
```

## 🏗️ Project Architecture

```
Library-Management-System/
├── 📁 api/                    # API routing and configuration
│   ├── urls.py               # Main API URL patterns
│   └── views.py              # API root view
│
├── 📁 catalog/               # Core library catalog management
│   ├── models.py             # Book, Author, Category models
│   ├── views.py              # Catalog viewsets with Swagger docs
│   ├── serializers.py        # API serialization logic
│   ├── filters.py            # Advanced filtering logic
│   ├── paginations.py        # Custom pagination settings
│   └── validators.py         # File upload validators
│
├── 📁 circulation/           # Book borrowing and return system
│   ├── models.py             # BorrowRecord, Fine models
│   ├── views.py              # Circulation management APIs
│   ├── serializers.py        # Circulation data serialization
│   ├── permissions.py        # Role-based permission classes
│   └── signals.py            # Automated fine calculations
│
├── 📁 users/                 # Authentication and user management
│   ├── models.py             # Custom User, Member models
│   ├── managers.py           # Custom user manager
│   ├── serializers.py        # User data serialization
│   └── views.py              # User management endpoints
│
├── 📁 library_management/    # Project settings and configuration
│   ├── settings.py           # Django settings (production-ready)
│   ├── urls.py               # Root URL configuration
│   ├── wsgi.py               # WSGI application entry point
│   └── asgi.py               # ASGI configuration (future WebSocket)
│
├── 📁 fixtures/              # Sample/seed data
│   └── catalog_data.json     # Sample books and authors
│
├── 📁 media/                 # User-uploaded files (Cloudinary)
│   ├── authors/photos/       # Author profile photos
│   ├── books/covers/         # Book cover images
│   └── members/profile_pics/ # Member profile pictures
│
├── 📁 staticfiles/           # Collected static files (production)
├── 📄 vercel.json            # Vercel deployment configuration
├── 📄 requirements.txt       # Python dependencies
├── 📄 manage.py              # Django management script
├── 📄 .env                   # Environment variables (not in git)
└── 📄 README.md              # This comprehensive guide
```

## 🌐 Production Deployment

### Vercel Configuration
```json
{
    "builds": [{
      "src": "library_management/wsgi.py",
      "use": "@vercel/python",
      "config": { 
        "maxLambdaSize": "15mb", 
        "runtime": "python3.11.3" 
      }
    }],
    "routes": [{
        "src": "/(.*)",
        "dest": "library_management/wsgi.py"
    }]
}
```

### Production Settings
- ✅ **DEBUG = False** for security
- ✅ **PostgreSQL** database (Supabase)
- ✅ **Cloudinary** for media storage
- ✅ **WhiteNoise** for static files
- ✅ **CORS** configuration for frontend
- ✅ **HTTPS** enforcement
- ✅ **Environment variables** for sensitive data

### Performance Optimizations
- **Database Indexing** on frequently queried fields
- **Query Optimization** with select_related and prefetch_related
- **Pagination** for large datasets
- **Caching** headers for static content
- **Cloudinary** automatic image optimization

## 🧪 Testing

Run the comprehensive test suite:
```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test catalog
python manage.py test circulation
python manage.py test users

# Run with coverage report
coverage run manage.py test
coverage report
coverage html
```

## 📈 Performance Metrics

- **Response Time:** < 200ms for most endpoints
- **Database Queries:** Optimized with prefetch/select_related
- **File Uploads:** Handled via Cloudinary CDN
- **API Rate Limiting:** Configurable per user role
- **Scalability:** Serverless deployment ready

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the Repository**
2. **Create Feature Branch** (`git checkout -b feature/amazing-feature`)
3. **Commit Changes** (`git commit -m 'Add amazing feature'`)
4. **Push to Branch** (`git push origin feature/amazing-feature`)
5. **Open Pull Request**

### Development Guidelines
- Follow **PEP 8** Python style guide
- Write **comprehensive tests** for new features
- Update **documentation** for API changes
- Use **meaningful commit messages**

## 📜 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## 🆘 Support & Contact

**Nazmul Hossain** - Full Stack Developer

- 📧 **Email:** [snazmulhossains24@gmail.com](mailto:snazmulhossains24@gmail.com)
- 🐙 **GitHub:** [@nazmulh24](https://github.com/nazmulh24)
- 💼 **LinkedIn:** [Nazmul Hossain](https://linkedin.com/in/nazmulh24)
- 🌐 **Portfolio:** [nazmulhossain.dev]()

**Project Repository:** [Library Management System](https://github.com/nazmulh24/Library_Management_System)

## 🙏 Acknowledgments

- **Django Community** for the excellent framework
- **Django REST Framework** for powerful API development
- **Swagger/OpenAPI** for comprehensive documentation
- **Vercel** for seamless deployment
- **Cloudinary** for media management
- **PostgreSQL & Supabase** for reliable database hosting

---

<div align="center">

### 🌟 If you found this project helpful, please consider giving it a star! ⭐

**Built with ❤️ by [Nazmul Hossain](https://github.com/nazmulh24)**

</div>
