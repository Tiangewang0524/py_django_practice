# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import Weather


class Spider1Spider(scrapy.Spider):
    name = 'weather_spider'
    allowed_domains = ['www.tianqihoubao.com']
    start_urls = ['http://www.tianqihoubao.com/lishi/nanjing/month/201505.html']

    def parse(self, response):
        # 获取所有天气信息
        weas = response.xpath('//div[@class="hd"]/div[1]/table/tr')

        # 将数据封装到item对象中
        item = Weather()
        for wea in weas:
            # 去掉第一行名称
            if wea.xpath('td[1]/a/text()').extract():
                item['date'] = wea.xpath('td[1]/a/text()').extract()[0].replace('\r\n', '').replace(' ', '')
                # 对date做进一步规范处理
                item['date'] = item['date'][:4] + '-' + item['date'][5:7] + '-' + item['date'][8:10]
                item['weather'] = wea.xpath('td[2]/text()').extract()[0].replace("\r\n", '').replace(' ', '')
                item['temperature'] = wea.xpath('td[3]/text()').extract()[0].replace("\r\n", '').replace(' ', '')
                item['wind'] = wea.xpath('td[4]/text()').extract()[0].replace('\r\n', '').replace(' ', '')

                yield item
                print(item)

        # 查找下一页的元素，获取URL
        next = response.xpath('//*[@id="content"]/p/a[2]/@href').extract()[0]
        url = response.urljoin(next)
        yield scrapy.Request(url=url, callback=self.parse, dont_filter=False)
