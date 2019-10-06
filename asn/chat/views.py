# chat/views.py
from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from . import cdns


def index(request):
    return render(request, 'chat/index.html', {})


def room(request, room_name):
    return render(request, 'chat/chatbox.html',
                  {"jQuery": cdns.jQuery213,
                   "jQueryNiceRoll": cdns.jQueryNiceRoll,
                   'room_name_json': mark_safe(json.dumps(room_name))}
                  )


def chatbox(request):
    return render(request, 'chat/chatbox.html', {"cdns": cdns.cdns})
