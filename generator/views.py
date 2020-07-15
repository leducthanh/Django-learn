from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

def home(request):
    return render(request,'generator/home.html')

def password(request):
    length = int(request.GET.get('length',8))
    key = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('upper'):
        key.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('number'):
        key.extend(list('1234567890'))
    if request.GET.get('special'):
        key.extend(list('!@#$%^&*()'))
    password = ""
    password = password.join([random.choice(key) for x in range(length)])

    return render(request,'generator/password.html',{'password':password})
def contact(request):
    return render(request,'generator/contact.html')
