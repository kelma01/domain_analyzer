import requests

def get_robots_txt(domain):
    res = requests.get(url=f"https://{domain}/robots.txt")
    return res.text
