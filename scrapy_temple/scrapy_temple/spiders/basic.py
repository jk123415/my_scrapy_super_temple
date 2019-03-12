# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest


# script = '''
# function main(splash, args)
#   assert(splash:go(args.url))
#   assert(splash:wait(0.5))
#   local html, next
#   item_list = {}
#   html = splash:html()
#   table.insert(item_list,html)
#   for i=1,3,1 do
#     next = splash:select('.btn-next')
#   	next:mouse_click{}
#   	assert(splash:wait(2))
#   	html = splash:html()
#   	table.insert(item_list,html)
#   end
#   return {
#     html = table.concat(item_list,",,,")
#     --png = splash:png(),
#     --har = splash:har(),
#   }
# end
# '''
# yield SplashRequest(
#    url,
#    self.parse,
#    endpoint='execute',
#    args={'lua_source': script})
# splash service html 接口
# http://192.168.99.100:8050/render.html?url=URL

class BasicSpider(scrapy.Spider):
    name = 'basic'
    allowed_domains = ['basic']
    start_urls = ['http://basic/']
    mongodb_db_name = ''

    def parse(self, response):
        pass

    # item必须包含name字段 用于判断采集是否成功
    # item必须包含url 字段 用于从mongodb数据库过虑重复网址
