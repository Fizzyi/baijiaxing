# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Xingshi_Item(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    xingshi = scrapy.Field()
    href = scrapy.Field()
    xingshi_zhongwen = scrapy.Field()


class Xingming_Item(scrapy.Item):
    name = scrapy.Field()
    the_same_people_number = scrapy.Field()
    boy_ratio = scrapy.Field()
    girl_ratio = scrapy.Field()
    five_elements = scrapy.Field()
    three_talents = scrapy.Field()
    xingshi = scrapy.Field()
