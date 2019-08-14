import requests

r = requests.get("http://images.china-pub.com/ebook7960001-7965000/7962875/zcover.jpg")
with open('zcover.jpg', 'wb') as f:
    f.write(r.content)
