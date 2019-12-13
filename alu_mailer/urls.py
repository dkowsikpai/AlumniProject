from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.mailer, name='mailer'),
    path('search.json', views.autocompleteModel, name='autocomplete-mailer'),
    path('email_manager', views.mail_sending_manager, name='mailing-manager-mailer'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
