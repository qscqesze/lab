# -*- coding: gbk -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render
from django.shortcuts import redirect
from user.models import User
import logging

def up_to_back(url):
    pos1 = 0
    pos2 = 0
    for i in range(0,len(url)):
        if url[i] == '/':
            pos2 = pos1
            pos1 = i
    if pos1 == 0:
        return "-1"
    new_url = ""
    for i in range(0,len(url)):
        if i >= pos2 and i < pos1:
            continue
        new_url += url[i]
    return new_url

def hello(request):
    context = {'user':request.COOKIES.get('user', '')}
    logging.debug(request)
    url = request.path[1:]
    if url == '':
        url = 'index.html'
    return render(request, url, context)

def login(request):
    if request.method == "POST":
        input_user = request.POST['user']
        input_pwd = request.POST['password']
        user = User.objects.filter(username__exact=input_user, password__exact=input_pwd)
        if user:
            response = HttpResponseRedirect('index.html')
            response.set_cookie('user', input_user, 3600)
            return response
            # return render(request, 'index.html', {'user': input_user})
        else:
            return render(request, 'login.html', {'status': 'ERROR Incorrect username or password'})
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        input_user = request.POST['user']
        input_pwd = request.POST['password']
        input_email = request.POST['email']
        User.objects.create(username=input_user,password=input_pwd,email=input_email)
        return HttpResponse('regist success!')
    return render(request, 'register.html')

def logout(request):
    logging.debug("logging out!!!!!!!")
    response = HttpResponseRedirect('index.html')
    response.delete_cookie('user')
    return response


if __name__ == '__main__':
    print(up_to_back('./problem/index.html'))