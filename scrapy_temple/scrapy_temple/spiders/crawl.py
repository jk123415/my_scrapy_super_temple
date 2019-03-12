# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CSpider(CrawlSpider):
    name = 'crawl'
    allowed_domains = ['basic']
    start_urls = ['http://basic/']
    mongodb_db_name = ''

    rules = (
        Rule(
            LinkExtractor(
                allow=r'Items/'
            ),
            callback='parse_item',
            follow=True),
    )

    def parse_item(self, response):
        # 必须包含name 字段
        # item必须包含url字段 用于从mongodb数据库过虑重复网址
        item = {}
        item['name'] = ''
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        item['url'] = response.url
        return item
