from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.PostApiManager.as_view(), name='posts_api'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
