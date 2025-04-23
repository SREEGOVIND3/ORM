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
