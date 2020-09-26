import requests
url="http://www.ip138.com/ips138.asp?ip="
try:
    r=requests.get(url+'202.204.80.112')
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except :
    print("爬取失败")