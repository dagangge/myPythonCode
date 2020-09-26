import requests

url="https://maoyan.com/board"
r=requests.get(url)
print(r.text)