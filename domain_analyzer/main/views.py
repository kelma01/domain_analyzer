from django.shortcuts import render
from django.http import *
from django.template import loader
from .forms import TextInputForm

def hello(request):
    return render(request, 'index.html')

def ip_addresses(request):
    result = None
    payload = None
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            pass
    else:
        form = TextInputForm()

    return render(request, 'ip-addresses.html')