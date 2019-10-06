from django.shortcuts import render, HttpResponse
import pyrebase

# Configuration Firebase

config = {
  "apiKey": "AIzaSyBKxSkkUfZ6DDiyDG3jkxxr6ElIGz_aAx8",
  "authDomain": "asn1822-bd628.firebaseapp.com",
  "databaseURL": "https://asn1822-bd628.firebaseio.com",
  "projectId": "asn1822-bd628",
  "storageBucket": "asn1822-bd628.appspot.com",
  "messagingSenderId": "921992085550",
  "appId": "1:921992085550:web:1a5314af6d42d721d39fbf",
  "measurementId": "G-X0WKY98NVJ"
}
firebase = pyrebase.initialize_app(config)
# print(firebase)
# Create your views here.


def login(request):
    # auth = firebase.auth()

    # Log the user in
    # user = auth.sign_in_with_email_and_password("dkowsikpai@gmail.com", "Dinesh@1969")
    return render(request, 'user_home/user_home.html')


def user_auth(request):
    auth = firebase.auth()

    # Log the user in
    try:
        user = auth.sign_in_with_email_and_password(request.POST['username'], request.POST['password'])
        return HttpResponse("Hi")
    except:
        return HttpResponse("Try")
