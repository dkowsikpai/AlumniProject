from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('login/', views.login, name='userAuth-login'),
    path('user_auth/', views.user_auth, name='userAuth-login')
]
