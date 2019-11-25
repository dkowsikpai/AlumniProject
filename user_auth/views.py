from django.shortcuts import render, HttpResponse, render_to_response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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
    return render(request, 'login/logged_in.html')


@login_required
def log_out(request):
    logout(request)
    return HttpResponse('Successfully Logged out')


def error_404(request, *args, **argv):
    response = render_to_response('error/error_404.html', {'data': 400})
    response.status_code = 404
    return response
