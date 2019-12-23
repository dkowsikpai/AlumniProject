from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Profile)
class ProfileDisplayPanel(admin.ModelAdmin):
    list_display = ['user', 'image']
