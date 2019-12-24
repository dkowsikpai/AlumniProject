from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Posts)
class PostDisplayPanel(admin.ModelAdmin):
    list_display = ['title', 'date', 'author', 'display']


@admin.register(Comment)
class CommentDisplayPanel(admin.ModelAdmin):
    list_display = ['post', 'content', 'display']
