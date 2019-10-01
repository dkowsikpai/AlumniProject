from django.conf.urls import url
from django.urls import path, re_path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    re_path(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]
