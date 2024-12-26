from django.shortcuts import render
from django.http import *
from django.template import loader

def hello(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())