from django.shortcuts import render

# Create your views here.


def welcome(request):
    print('111')
    return render(request, 'welcome.html',{"key1":1,"key2":2,"key3":{1,2,3}})

def case_list(request):
    return render(request,'case_list.html')


def home(request):
    return render(request,'welcome.html',{"whichHTML": "Home.html","oid": ""})

def child(request,eid,oid):
    return render(request,eid)

def login(request):
    return render(request,'login.html')