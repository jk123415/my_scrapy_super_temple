# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CSpider(CrawlSpider):
    name = 'cra'
    #allowed_domains = ['basic']
    start_urls = ['http://sousuo.gov.cn/list.htm?q=&n=100&p=0&t=paper&sort=pubtime&childtype=&subchildtype=&pcodeJiguan=&pcodeYear=&pcodeNum=&location=&searchfield=&title=&content=&pcode=&puborg=&timetype=timeqb&mintime=&maxtime=']
    mongodb_col_name = 'a_20190312'

    rules = (
        Rule(
            LinkExtractor(
                allow=r'q=&n=100&p=\d+&t=paper&sort=pubtime&childtype=&subchildtype=&pcodeJiguan=&pcodeYear=&pcodeNum=&location=&searchfield=&title=&content=&pcode=&puborg=&timetype=timeqb&mintime=&maxtime='
            ),
            follow=True),
        Rule(
            LinkExtractor(
                restrict_css=".info a",
            ),
            callback='parse_item',
            follow=False),
    )

    def parse_item(self, response):
        # 必须包含name 字段
        # item必须包含url字段 用于从mongodb数据库过虑重复网址
        item = {}
        item['name'] = response.css('.bd1').re_first('colspan="3">(.*?)</td>')
        item['body'] = response.css('.b12c p::text').getall()
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        item['url'] = response.url
        return item
