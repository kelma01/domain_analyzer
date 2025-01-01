import dns.resolver

record_list = ["A", "AAAA", "NS", "CNAME", "MX", "TXT", "SOA", "PTR"] #can be added for any other purpose

records = []

def get_records(domain):
    for record in record_list:
        try:
            result = dns.resolver.resolve(domain, record)
            for i in result:
                type = str(i.to_text).split(" ")[6]
                records.append([type, i.to_text])
        except Exception:
            pass
    return records