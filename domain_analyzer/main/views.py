from django.shortcuts import render
from django.http import *
from django.template import loader
from .forms import TextInputForm

from .tools.ip_address import get_ip
from .tools.port_scanner import scan_ports
from .tools.ssl_scanner import scan_ssl_cert
from .tools.whois_search import get_whois

def hello(request):
    return render(request, 'index.html')

def analyze_domain(request):
    payload = None
    if request.method == 'GET':
        return render(request, 'domain_analyzer.html')
    elif request.method == 'POST':
        form = TextInputForm(request.POST)
        if form.is_valid():
            domain = form.cleaned_data['user_input']
            ipv4 = get_ip(domain)
            ssl_validity, ssl_not_valid_after = scan_ssl_cert(domain)
            ssl_not_valid_after = str(ssl_not_valid_after)[0:10].replace("-","/")
            whois_response = get_whois(domain) #[[],[],[],[]]
            for i in whois_response:
                i[0] = str(i[0]).replace("_", " ").title()

            ports = [['80', 'http'],['443', 'https']] #TODO: ports = scan_ports(ipv4)
             
            payload = {
                "IPv4": ipv4,
                "SSL Certificate Validity": ssl_validity,
                "SSL Certificate Not Valid After": ssl_not_valid_after
            }


    else:
        form = TextInputForm()

    return render(request, 'domain_analyzer.html', {'form': form, 'result': payload, 'open_ports': ports, 'whois_response': whois_response})