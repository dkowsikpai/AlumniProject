from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.forum, name='forum'),
    path('get_comments/', views.get_comments, name='get-comments'),
    path('submit_like/', views.submit_like, name='submit-like'),
    path('submit_comment/', views.submit_comment, name='submit-comment'),
    path('reg-project/', views.reg_project, name='reg-project'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
