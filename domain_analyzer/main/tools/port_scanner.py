import nmap

port_list = [21,22,23,25,53,80,110,111,135,139,143,443,445,993,995,1723,3306,3389,5900,8080]
port_list = [80, 443]
result = []

def scan_ports(ip):
    scanner = nmap.PortScanner()

    for port in port_list:
        res = scanner.scan(ip, str(port))
        if res['scan'][str(ip)]['tcp'][port]['state'] == "open" and res['scan'][str(ip)]['status']['state'] == "up":
            result.append([port, res['scan'][str(ip)]['tcp'][port]['name']])
        
    return result