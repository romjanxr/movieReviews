from django.contrib import admin

from movie.models import Category, Movie, Review

# Register your models here.

admin.site.register(Movie)
admin.site.register(Review)

admin.site.register(Category)
