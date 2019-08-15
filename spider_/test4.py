from lxml import etree

html = etree.parse('http://www.12306.cn/mormhweb/', etree.HTMLParser())

content_list = html.getroot().xpath("/html/body/div[@id='page']/div[@id='indexLeft']/div[@id='indexLeftB']/div[@id='indexLeftBL']/ul[@class='leftItem']/li[*]/a/text()")
for content in content_list:
    print(content)