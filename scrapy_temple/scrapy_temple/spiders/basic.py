# -*- coding: utf-8 -*-
import scrapy


class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['basic']
    start_urls = ['http://basic/']

    def parse(self, response):
        pass
