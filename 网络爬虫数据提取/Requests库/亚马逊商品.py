import requests
def getHtmlText(url):
       try:
           kv={'user-agent':'Mozilla/5.0'}
           r=requests.get(url,headers=kv)
           r.raise_for_status()
           r.encoding=r.apparent_encoding
           return r.text
       except:
           return "产生异常"
url="https://www.amazon.cn/dp/B07MD8NGWV"
print(getHtmlText(url))