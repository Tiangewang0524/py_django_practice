# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem


class Spider1Spider(scrapy.Spider):
    name = 'spider_1'
    allowed_domains = ['product.china-pub.com']
    start_urls = ['http://product.china-pub.com/cache/browse2/59/1_2_59_0.html']

    def parse(self, response):
        # 获取所有书籍
        books = response.xpath('//li[@class="result_name"]/..')

        # 将数据封装到item对象中
        item = MyspiderItem()
        for book in books:
            # 从书籍中解析信息
            item['name'] = book.xpath('./li[@class="result_name"]/a[1]/text()').extract()[0]
            item['info'] = book.xpath('./li[@class="result_name"]/../li[2]/text()').extract()[0]
            item['price'] = \
            book.xpath('./li[@class="result_book"]/ul/li[@class="book_dis"]/b/text()').re('￥(\d*\.\d*)')[0]
            yield item

        # 查找下一页的元素，获取URL
        next = response.css('#right .pro_pag a::attr("href")').extract()[-1]
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
