from django.shortcuts import render
from django.http import *
from django.template import loader
from .forms import TextInputForm
import nmap

from .tools.ip_address import get_ip
from .tools.port_scanner import scan_ports

def hello(request):
    return render(request, 'index.html')

def ip_addresses(request):
    payload = None
    if request.method == 'GET':
        return render(request, 'ip_addresses.html')
    elif request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            user_input = form.cleaned_data['user_input']
            ipv4 = get_ip(user_input)
            #ports = scan_ports(ipv4)
            ports = [[80, 'http'][443, 'https']]

            payload = {
                "IPv4": ipv4
            }

    else:
        form = TextInputForm()

    return render(request, 'ip_addresses.html', {'form': form, 'result': payload, 'open_ports': ports})