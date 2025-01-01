import requests

result = []

def get_subdomains(domain):
	subdomains = None
	
	with open('main/tools/subdomain_list.txt', 'r') as file:
		tmp = file.read()
		subdomains = tmp.splitlines()

		for subdomain in subdomains:
			url = f"https://{subdomain}.{domain}"

			try:
				req = requests.get(url)
				if req.status_code == 200:
					result.append(url)
			except Exception:
				pass
		
		return result