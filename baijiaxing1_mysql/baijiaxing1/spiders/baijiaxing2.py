# -*- coding: utf-8 -*-
import scrapy

from baijiaxing1.items import Xingshi_Item


class Baijiaxing2Spider(scrapy.Spider):
    name = 'baijiaxing2'
    # allowed_domains = ['resgain.net/xmdq.html']
    start_urls = ('http://www.resgain.net/xmdq.html',)

    def parse(self, response):
        content = response.xpath('//div[@class="col-xs-12"]/a')

        for i in content:
            # xingshi = i.split('.')[0].split('/')[-1]
            xingshi = i.xpath('./@href').extract()[0].split('.')[0].split('/')[-1]

            href = 'http:' + i.xpath('./@href').extract()[0]
            item = Xingshi_Item()
            item['xingshi'] = xingshi
            item['href'] = href
            item['xingshi_zhongwen'] = i.xpath('./text()').extract()[0].split('姓名')[0]

            yield item
