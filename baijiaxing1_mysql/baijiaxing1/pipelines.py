# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from baijiaxing1.items import Xingshi_Item, Xingming_Item


class XingShiPipeline(object):
    def __init__(self,host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    def process_item(self, item, spider):
        if isinstance(item, Xingshi_Item):
            sql = 'INSERT INTO baijiaxing(xingshi,href,xingshi_zhongwen) VALUES (%s,%s,%s);'
            self.cursor.execute(sql,(item['xingshi'],str(item['href']),item['xingshi_zhongwen']))
            self.db.commit()
            return item
        elif isinstance(item,Xingming_Item):
            sql = 'SELECT id FROM xingshi WHERE xingshi = %s' %item['xingshi']
            xingshi_id = self.cursor.execute(sql)
            sql = 'INSERT INTO xingming(name,the_same_people_number,boy_ratio,girl_ratio,five_elements,three_talents,xingshi_id)values (%s,%s,%s,%s,%s,%s,%s);'
            self.cursor.execute(sql,(item['name'],item['the_same_people_number'][0],item['boy_ratio'][0],item['girl_ratio'][0],item['five_elements'][0],item['three_talents'],int(xingshi_id)))
            self.db.commit()
            return item

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('PYMYSQL_HOST'),
            database=crawler.settings.get('PYMYSQL_DATABASE'),
            user=crawler.settings.get('PYMYSQL_USER'),
            password=crawler.settings.get('PYMYSQL_PASSWORD'),
            port=crawler.settings.get('PYMYSQL_PORT'),
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.user, self.password, self.database, port=self.port)
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

