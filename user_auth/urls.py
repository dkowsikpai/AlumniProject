from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login_auth/', views.auth, name='auth'),
    path('logged_in/', views.logged_in, name='log'),
    path('logout/', views.log_out, name='log_out'),
    path('send/', views.send_email, name='send'),
    path('profile/', views.profile, name='profile'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
