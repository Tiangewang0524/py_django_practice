from urllib.request import urlopen
from bs4 import BeautifulSoup

r = urlopen('http://product.china-pub.com/cache/browse2/59/1_2_59_0.html')

bs_obj = BeautifulSoup(r.read().decode('gb2312', errors='ignore'), 'html.parser')

text_list = bs_obj.find_all('li', 'result_name')
list_1 = []
list_2 = []
dict_1 = dict()

for text in text_list:
    list_1.append(text.get_text().partition('即时配发')[0])

price_list = bs_obj.find_all('li', 'book_price')

for price in price_list:
    list_2.append(price.get_text())

# print(list_1, list_2)

for i in range(len(list_1)):
    dict_1[list_1[i]] = list_2[i]

print(dict_1)


