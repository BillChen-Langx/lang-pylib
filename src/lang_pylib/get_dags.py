import requests

p = requests.get("http://google.com", timeout=5)
print(p.status_code)
