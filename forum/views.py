from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


from django.core import serializers
# Create your views here.


@login_required
def forum(request):
    db = Posts.objects.filter(display=True).order_by('-date')
    content = {'posts': db}
    return render(request, 'forum.html', content)


@login_required
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


@login_required
def submit_like(request):
    id = request.POST.get('id')
    user = request.user
    resp = {}
    try:
        post = Posts.objects.get(id=id)
        post.likes.add(user)
        post.save()
        resp = {'is_done': True, 'tot_likes': post.total_likes()}
    except:
        resp = {'is_done': False}
    return JsonResponse(resp, safe=False)


@login_required
def submit_comment(request):
    id = request.POST.get('id')
    data = request.POST.get('data')
    user = request.user
    try:
        post = Posts.objects.get(id=id)
        db = Comment.objects.create(post=post, user=user, content=data)
        db.save()
        resp = {'is_done': True}
    except:
        resp = {'is_done': False}
    return JsonResponse(resp, safe=False)


def reg_project(request):
    if request.method == 'POST':
        form = ProjectSubmitForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            event = Posts.objects.create(
                title=data['title'],
                subtitle=data['subtitle'],
                content=data['content'],
                author=request.user,
                image1=data['img1'],
                image2=data['img2'],
                image3=data['img3']
            )
            event.save()
            return redirect('/forum/')

    else:
        form = ProjectSubmitForm()
    return render(request, 'reg_proj.html', {'form': form})

