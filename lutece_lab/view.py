from django.http import HttpResponse
from django.shortcuts import render
import logging

def hello(request):
    logging.debug(request)
    url = request.path[1:]
    if url == '':
        url = 'index.html'
    return render(request, url)

def news(request):
    return render(request, 'news.html')