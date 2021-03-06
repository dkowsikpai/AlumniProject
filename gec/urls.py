"""gec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import urls
from django.contrib import admin
from django.urls import path, include
from user_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth.urls')),
    path('mailer/', include('alu_mailer.urls')),
    path('forum/', include('forum.urls')),
    path('api/', include('api_manager.urls')),

]

urls.handler404 = 'user_auth.views.error_404'
urls.handler500 = 'user_auth.views.error_404'
