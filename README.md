# Ex02 Django ORM Web Application
## Date: 18-04-2025

## AIM
To develop a Django application to store and retrieve data from Movies Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import Movie, MovieAdmin
admin.site.register(Movie, MovieAdmin)

models.py

from django.db import models
from django.contrib import admin

class Movie(models.Model):
    movie_id = models.CharField(max_length=10, help_text="Movie ID")
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    release_year = models.IntegerField()
    rating = models.FloatField()
    
    def __str__(self):
        return self.title

class MovieAdmin(admin.ModelAdmin):
    list_display = ('movie_id', 'title', 'genre', 'release_year', 'rating')
```
## OUTPUT
![alt text](<Screenshot 2025-04-23 182604.png>)


## RESULT
Thus the program for creating a database using ORM hass been executed successfully
