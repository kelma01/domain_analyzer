import socket

def get_ip(domain):
    try:
        ipv4_addresses = socket.getaddrinfo(domain, 443, socket.AF_INET)
        ipv4_list = [addr[4][0] for addr in ipv4_addresses]
        result = list(set(ipv4_list))[0]

        return {
            "IPv4": result
        }
    except socket.gaierror as e:
        return {"error": str(e)}

