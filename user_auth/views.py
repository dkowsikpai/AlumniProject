from django.shortcuts import render, HttpResponse, render_to_response, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
from django.template import RequestContext


def home(request):
    return render(request, 'login/login_home.html')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return HttpResponse('Success')
    else:
        # Return an 'invalid login' error message.
        return HttpResponse('failed')


@login_required
def logged_in(request):
    return redirect('/forum')


@login_required
def log_out(request):
    logout(request)
    return redirect('/')


def error_404(request, *args, **argv):
    response = render_to_response('error/error_404.html', {'data': 400})
    response.status_code = 404
    return response


def send_email(request):
    # subject = "Hey there"  # request.POST.get('subject', '')
    # message = "How are you?"  # request.POST.get('message', '')
    # from_email = "dkowsikpai@gmail.com"  # request.POST.get('from_email', '')
    # if subject and message and from_email:
    #     try:
    #         send_mail(subject, message, from_email, ['dkowsikpai@gmail.com'])
    #     except BadHeaderError:
    #         return HttpResponse('Invalid header found.')
    #     return HttpResponse('Sent')
    # else:
    #     # In reality we'd use a form class
    #     # to get proper validation errors.
    #     return HttpResponse('Make sure all fields are entered and valid.')

    message = "hey there"
    mail_subject = 'Activate your blog account.'
    to_email = "dkowsikpai@gmail.com"
    email = EmailMessage(mail_subject, message, to=[to_email], from_email="dkowsikpai.coder@gmail.com")
    email.send()
    return HttpResponse('success')


@login_required
def profile(request, username):
    db = Profile.objects.get(user=User.objects.get(username=username))
    return render(request, 'profile.html', {'data': db})
