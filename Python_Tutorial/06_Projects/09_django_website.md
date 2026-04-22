# Project 3: Building a Website with Django

## What is Django?
A Python web framework for building websites fast.

## Installation
```bash
pip install django
```

## Create Project
```bash
django-admin startproject mysite
cd mysite
python manage.py migrate
python manage.py runserver
```

## Project Structure
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
```

## Create App
```bash
python manage.py startapp blog
```

## Views (urls.py)
```python
# mysite/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
]
```

## Views (views.py)
```python
# blog/views.py
from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to my site!")

def about(request):
    return HttpResponse("About page")
```

## Templates
```html
<!-- blog/templates/blog/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>My Site</title>
</head>
<body>
    <h1>Welcome!</h1>
    <p>Hello, {{ name }}</p>
</body>
</html>
```

## Database Models
```python
# blog/models.py
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
```

## Admin
```python
# blog/admin.py
from django.contrib import admin
from .models import Post

admin.site.register(Post)
```

## Key Django Features
- Built-in admin panel
- Database ORM
- User authentication
- Form handling
- Security features

## Next Steps
1. Read Django documentation
2. Build a blog
3. Learn about deployment
4. Learn REST API with Django REST Framework