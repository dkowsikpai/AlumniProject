from django.shortcuts import render, HttpResponse
from .models import *
from django.http import JsonResponse
from django.core import serializers
# Create your views here.


def forum(request):
    db = Posts.objects.filter(display=True).order_by('-date')
    content = {'posts': db}
    return render(request, 'forum.html', content)


def get_comments(request):
    id = request.POST.get('id')
    post = Posts.objects.get(id=id)
    db = Comment.objects.filter(post=post).order_by('-id')
    l = []
    for i in db:
        dic = {'username': i.user.first_name + ' ' + i.user.last_name, 'content': i.content, "id": i.id, "user_pic": i.user.profile.image.url}
        l.append(dic)
    # data = serializers.serialize("json", l)
    return JsonResponse(l, safe=False)
