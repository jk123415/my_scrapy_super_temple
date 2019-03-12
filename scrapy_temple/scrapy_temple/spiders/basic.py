# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['basic']
    start_urls = ['http://basic/']
    mongodb_db_name = ''

    def parse(self, response):
        pass

    # item必须包含name字段 用于判断采集是否成功
    # item必须包含url 字段 用于从mongodb数据库过虑重复网址
