from django.shortcuts import render
from django.http import *
from django.template import loader
from .forms import TextInputForm

from .tools.ip_address import get_ip
from .tools.port_scanner import scan_ports
from .tools.ssl_scanner import scan_ssl_cert
from .tools.whois_search import get_whois
from .tools.dns_records import get_records
from .tools.subdomain_finder import get_subdomains
from .tools.robots_parser import get_robots_txt

def hello(request):
    return render(request, 'index.html')

def analyze_domain(request):
    if request.method == 'GET':
        return render(request, 'domain_analyzer.html')
    elif request.method == 'POST':
        form = TextInputForm(request.POST)

        if form.is_valid():

            #RETRIEVING DATA
            domain = form.cleaned_data['user_input']

            ipv4 = get_ip(domain)
            ssl_info, ssl_validity_status = scan_ssl_cert(domain)
            whois_response = get_whois(domain)
            ports = scan_ports(ipv4)
            dns_records = get_records(domain)
            subdomains = get_subdomains(domain)
            robots_info = [get_robots_txt(domain)]
             
            #PAYLOADS
            ip_payload = {
                "IPv4:": ipv4,
            }
            ssl_payload = {
                "Validity Status": ssl_validity_status,
                "Hostname": ssl_info["server_scan_results"][0]["server_location"]["hostname"],
                "Port": ssl_info["server_scan_results"][0]["server_location"]["port"],
                "IP Address": ssl_info["server_scan_results"][0]["server_location"]["ip_address"],
                "Not Valid After": str(ssl_info["server_scan_results"][0]["scan_result"]["certificate_info"]["result"]["certificate_deployments"][0]["received_certificate_chain"][0]["not_valid_after"]).replace("T", " ").replace("Z", "").replace("-","/"),
                "SAN": ssl_info["server_scan_results"][0]["scan_result"]["certificate_info"]["result"]["certificate_deployments"][0]["received_certificate_chain"][0]["subject_alternative_name"]["dns_names"]
            }
    else:
        form = TextInputForm()

    return render(request, 'domain_analyzer.html', {'form': form, 'ip_info': ip_payload, 'ssl_info': ssl_payload, 'open_ports': ports, 'whois_response': whois_response, 'dns_records': dns_records, 'subdomains': subdomains, 'robots': robots_info})