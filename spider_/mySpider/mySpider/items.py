# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    info = scrapy.Field()
    price = scrapy.Field()


class NBA_Item(scrapy.Item):
    player_team = scrapy.Field()
    player_name = scrapy.Field()
    player_num = scrapy.Field()
    player_position = scrapy.Field()
    player_height = scrapy.Field()
    player_weight = scrapy.Field()
    # PPG = scrapy.Field()
    # RPG = scrapy.Field()
    # APG = scrapy.Field()
    player_contract = scrapy.Field()
    player_salary = scrapy.Field()
    career_play = scrapy.Field()
    career_minute = scrapy.Field()
    FG = scrapy.Field()
    Three_PT = scrapy.Field()
    FT = scrapy.Field()
    RPG = scrapy.Field()
    APG = scrapy.Field()
    SPG = scrapy.Field()
    BPG = scrapy.Field()
    PTs = scrapy.Field()


class BookSpider(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    content = scrapy.Field()