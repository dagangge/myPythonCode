import requests
def getHtmlText(url):
       try:
           r=requests.get(url,timeout=30)
           r.raise_for_status()
           r.encoding=r.apparent_encoding
           return r.text
       except:
           return "产生异常"
url="https://item.jd.com/7652013.html"
print(getHtmlText(url))