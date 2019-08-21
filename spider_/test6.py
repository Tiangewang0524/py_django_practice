import requests

h = requests.get('https://nba.hupu.com/players/russellwestbrook-3016.html')
print(h.text)