# -*- coding: utf-8 -*-
from urllib.parse import urljoin

import scrapy

from baijiaxing1.items import Xingshi_Item, Xingming_Item


class SpiderXingmingSpider(scrapy.Spider):
    name = 'spider_xingming'
    # allowed_domains = ['www.resgain.net/xmdq.html']
    start_urls = ('http://www.resgain.net/xmdq.html',)

    def parse(self, response):
        content = response.xpath('//div[@class="col-xs-12"]/a/@href').extract()

        for i in content:
            page = 0
            # xingshi = i.split('.')[0].split('/')[-1]
            href = 'http:' + i
            # item = Xingshi_Item()
            # item['xingshi'] = xingshi
            # item['href'] = href

            base = href.split('/name')[0] + '/name_list_'

            while page < 10:
                url = base + str(page) + '.html'
                page += 1
                yield scrapy.Request(url, callback=self.parse_in_html)
            # parse_in_html(href, xingshi_id, cursor, db)

    # 解析每一页
    def parse_in_html(self, response):
        person_info = response.xpath('//div[@class="col-xs-12"]/a')
        base_url = 'http://'+response.url.split('/')[2]
        xingshi = response.url.split('/')[2].split('.')[0]
        for every_one in person_info:
            name = every_one.xpath('./text()').extract()[0]
            href = every_one.xpath('./@href').extract()[0]
            the_person_info_url =base_url + href
            the_item = Xingming_Item()
            the_item['name'] = name
            the_item['xingshi'] = xingshi
            yield scrapy.Request(the_person_info_url, meta={'the_item': the_item}, callback=self.parse_every_html)


    def parse_every_html(self, response):
        the_item = response.meta['the_item']
        the_same_people_number = \
        response.xpath('//div[@class="navbar-brand"]/text()').extract_first().split('人')[0].split('有')[1]
        boy_ratio = \
        response.xpath('//div[@class="progress"]/div[contains(@class,progress-bar)]/text()').extract()[0].split('情况')[0]
        girl_ratio = \
        response.xpath('//div[@class="progress"]/div[contains(@class,progress-bar)]/text()').extract()[1].split('情况')[0]
        five_elements = response.xpath('//div[@class="panel-body"]/div[@class="col-xs-6"]/blockquote/text()').extract()[
            0]
        three_talents = response.xpath('//div[@class="panel-body"]/div[@class="col-xs-6"]/blockquote/text()').extract()[
            1]
        the_item['the_same_people_number'] = the_same_people_number,
        the_item['boy_ratio'] = boy_ratio,
        the_item['girl_ratio'] = girl_ratio,
        the_item['five_elements'] = five_elements,
        the_item['three_talents'] = three_talents

        yield the_item
