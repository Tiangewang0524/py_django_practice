# -*- coding: utf-8 -*-
import scrapy, time
from mySpider.items import Food


class Spider1Spider(scrapy.Spider):
    name = 'food_spider'
    allowed_domains = ['i.boohee.com']
    start_urls = ['http://i.boohee.com/food/group/']

    def parse(self, response):
        url_list = response.xpath('//*[@id="main"]/div/div[1]/ul/li/a/@href').extract()

        # 第一分类条目总览
        for url in url_list:
            field_url = 'http://i.boohee.com' + url
            # print(field_url)
            # time.sleep(1)
            yield scrapy.Request(url=field_url, callback=self.parse_detail)

        # 第二分类条目总览
        for i in range(1, 132):
            field_url = 'http://i.boohee.com/food/view_group/' + str(i)
            yield scrapy.Request(url=field_url, callback=self.parse_detail)

    def parse_detail(self, response):
        # 保留该类目总的原始地址，不含分页
        if 'page' not in response.url:
            url_temp = str(response.url)
        # 获取所有食品信息
        foods = response.xpath('//*[@id="main"]/div/div[2]/ul')
        if foods:
            names = foods.xpath('li/div[2]/h4/a/text()')
            calories = foods.xpath('li/div[2]/p/text()')

            # 将数据封装到item对象中
            item = Food()

            for name, calorie in zip(names, calories):
                item['name'] = name.extract()
                item['calorie'] = calorie.extract()

                yield item
                print(item)

        # 查找下一页的元素，获取URL
        for i in range(2, 11):
            i = str(i)
            next = url_temp + '?page=' + i
            # print(next)
            url = response.urljoin(next)
            yield scrapy.Request(url=url, callback=self.parse_detail, dont_filter=False)
