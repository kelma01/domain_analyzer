import whois
import json

def get_whois(domain):

    key_values = []

    w = whois.whois(domain)

    json_output = json.loads(str(w))

    for key in json_output:
        key_values.append([key, json_output[key]])

    return key_values
