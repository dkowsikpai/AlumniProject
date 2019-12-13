from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
import simplejson
# Create your views here.


def mailer(request):
    return render(request, 'mailer.html')


def autocompleteModel(request):
    search_qs = User.objects.filter(username__startswith=request.GET['search'])
    results = []
    for r in search_qs:
        results.append(r.username)
    resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')


def mail_sending_manager(request):
    data_email = request.POST['email']
    print(data_email)
    # for each in data_email mail function should run
    return HttpResponse('success')
