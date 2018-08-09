from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    context = {}
    context['title'] = 'lutece.lab'
    return render(request, 'index.html', context)

def news(request):
    return render(request, 'news.html')