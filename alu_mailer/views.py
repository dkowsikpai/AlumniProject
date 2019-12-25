from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
import simplejson
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def mailer(request):
    return render(request, 'mailer.html')


@login_required
def autocompleteModel(request):
    search_qs = User.objects.filter(username__startswith=request.GET['search'])
    results = []
    for r in search_qs:
        results.append(r.username)
    resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')


@login_required
def mail_sending_manager(request):
    data_email = request.POST['email']
    print(data_email)
    # for each in data_email mail function should run
    return HttpResponse('success')
