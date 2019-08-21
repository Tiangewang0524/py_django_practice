# -*- coding: utf-8 -*-
import scrapy, logging
import time
from mySpider.items import NBA_Item


class NBA_Spider(scrapy.Spider):
    item_a = dict()
    item_a['player_name'] = 'kevin'
    name = 'nba_spider'
    allowed_domains = ['hupu.com']
    start_urls = ['https://nba.hupu.com/players/rockets']

    def parse(self, response):
        # 获取所有球员
        # players = response.xpath('//li[@class="result_name"]/..')
        url_list = response.xpath('//span[@class="team_name"]/a/@href').extract()
        player_team_list = response.xpath('//span[@class="team_name"]/a/text()').extract()

        for url, player_team in zip(url_list, player_team_list):
            team_url = url
            yield scrapy.Request(url=team_url, meta={'player_team': player_team}, callback=self.parse_detail)

    def parse_detail(self, response):
        temp_list = []
        print("爬虫工作中，正在爬取" + response.meta['player_team'] + "信息。")
        time.sleep(1)
        item = NBA_Item()
        item['player_team'] = response.meta['player_team']
        player_name_list = response.xpath('//td[@class="left"][1]//a/text()').extract()
        player_num_list = response.xpath('//tr[not(@class)]/td[3]').extract()
        # 给没有提供号码的球员赋值为NULL，一般为新秀。
        for each_num in player_num_list:
            each_num = each_num.replace('<td>', '').replace('</td>', '')
            if each_num == '':
                each_num = 'NULL'
            temp_list.append(each_num)
        player_num_list = temp_list
        # print(player_num_list)
        player_pos_list = response.xpath('//tr[not(@class)]/td[4]/text()').extract()
        player_height_list = response.xpath('//tr[not(@class)]/td[5]/text()').extract()
        player_weight_list = response.xpath('//tr[not(@class)]/td[6]/text()').extract()
        player_cont_list = response.xpath('//td[@class="left"][2]/text()').extract()
        # 给没有提供合同的球员赋值为NULL，一般为球员列表的最后几名球员。
        len_a = len(player_name_list)
        len_b = len(player_cont_list)
        if len_a != len_b:
            for i in range(abs(len_a - len_b)):
                player_cont_list.append('NULL')
        # print(player_cont_list)
        player_sal_list = response.xpath('//td[@class="left"][2]/b/text()').extract()
        player_url_list = response.xpath('//td[@class="left"][1]//a/@href').extract()

        zip_player = zip(player_name_list, player_num_list, player_pos_list, player_height_list, player_weight_list,
                         player_cont_list, player_sal_list, player_url_list)
        for player_name, player_num, player_position, player_height, player_weight, player_contract,\
            player_salary, player_url in zip_player:
            item['player_name'] = player_name
            item['player_num'] = player_num
            item['player_position'] = player_position
            item['player_height'] = player_height
            item['player_weight'] = player_weight
            item['player_contract'] = player_contract
            item['player_salary'] = player_salary
            # print(item)

            item_str = str(item)
            if item['player_salary'] != '本年薪金：89万美元' and item['player_salary'] != '本年薪金：7万美元' :
                yield scrapy.Request(url=player_url, meta={'item': item_str}, callback=self.parse_stat)
            # 新秀不做职业生涯数据的爬取
            else:
                item['career_play'] = '该球员为新秀，从未在NBA出场过。'
                # print(item)
                yield item

    def parse_stat(self, response):
        print("爬虫工作中，正在爬取" + str(eval(response.meta['item'])['player_name']) + "信息。")
        career_play = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[1]/text()').extract()
        item = eval(response.meta['item'])
        if career_play:
            career_minute = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[2]/text()').extract()[0]
            FG = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[4]/text()').extract()[0]
            Three_PT = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[6]/text()').extract()[0]
            FT = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[8]/text()').extract()[0]
            RPG = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[9]/text()').extract()[0]
            APG = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[10]/text()').extract()[0]
            SPG = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[11]/text()').extract()[0]
            BPG = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[12]/text()').extract()[0]
            PTs = response.xpath('//*[@id="in_box"]/div/div[1]/table[1]/tbody/tr[3]/td[15]/text()').extract()[0]

            # item = NBA_Item()
            item['career_play'] = '职业生涯每赛季场均出场'+ str(int(float(career_play[0]))) + '场'
            item['career_minute'] = '职业生涯场均出战' + career_minute + '分钟'
            item['FG'] = '投篮命中率为'+ FG
            item['Three_PT'] = '三分命中率为' + Three_PT
            item['FT'] = '罚球命中率为' + FT
            item['RPG'] = '场均篮板' + RPG + '个'
            item['APG'] = '场均助攻' + APG + '次'
            item['SPG'] = '场均抢断' + SPG + '次'
            item['BPG'] = '场均盖帽' + BPG + '个'
            item['PTs'] = '场均得分' + PTs + '分'

        # 对于在NBA从未出战过的球员不做职业生涯数据的爬取
        else:
            item['career_play'] = '该球员从未在NBA出场过。'
        print(item)

        yield item

