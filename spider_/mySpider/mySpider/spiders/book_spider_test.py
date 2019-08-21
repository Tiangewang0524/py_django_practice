# -*- coding: utf-8 -*-
import scrapy, re
from mySpider.items import MyspiderItem


class BookSpider(scrapy.Spider):
    name = 'book_spider_test'
    allowed_domains = ['product.china-pub.com']
    start_urls = ['http://product.china-pub.com/cache/browse2/59/1_2_59_0.html']

    def parse(self, response):
        # 获取所有书籍
        books = response.xpath('//li[@class="result_name"]/..')
        url_list = response.xpath('//li[@class="result_name"]/a/@href').extract()

        # 将数据封装到item对象中
        item = MyspiderItem()
        for book, url in zip(books, url_list):
            # 从书籍中解析信息
            item['name'] = book.xpath('./li[@class="result_name"]/a[1]/text()').extract()[0]
            # item['info'] = book.xpath('./li[@class="result_name"]/../li[2]/text()').extract()[0]
            item['price'] = '¥' + \
            book.xpath('./li[@class="result_book"]/ul/li[@class="book_dis"]/b/text()').re('￥(\d*\.\d*)')[0]
            # print(item)
            item_1 = str(item)
            yield scrapy.Request(url=url, meta={'item': item_1}, callback=self.parse_content, dont_filter=False)

            # print(type(item_1))

            # yield item

        # 查找下一页的元素，获取URL
        next = response.css('#right .pro_pag a::attr("href")').extract()[-1]
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)


    def parse_content(self, response):
        print("正在爬取书:" + str(eval(response.meta['item'])['name']) + "的信息。")
        item = eval(response.meta['item'])
        content = response.xpath('//*[@id="con_a_1"]/div[6]/div[1]/text()').extract()
        if content:
            content = [''.join(re.split(r"\n|\r|\t|\\u3000| ", x)) for x in content]
            content = [x.strip() for x in content if x.strip() != '']
            item['content'] = content
        else:
            item['content'] = ['无']

        print(item)
        yield item

