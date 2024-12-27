from django.shortcuts import render
from django.http import *
from django.template import loader
from .forms import TextInputForm

from .tools.ip import get_ip

import json

def hello(request):
    return render(request, 'index.html')

def ip_addresses(request):
    result = None
    payload = None
    if request.method == 'POST':
        form = TextInputForm(request.POST)
        #if form.is_valid():
        print(dir(form))
        print(form.changed_data['user_input'])
        """ user_input = form.cleaned_data['user_input']
        json_result = get_ip(user_input)
        result = json.loads(json_result)
        print(result) """
    else:
        form = TextInputForm()

    return render(request, 'ip-addresses.html', {'form': form, 'result': payload})