import requests
r=requests.get("https://python123.io/ws/demo.html")
r.text
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
print(soup.prettify())
for x in soup.find_all('a'):
    print(x.get('href'))

