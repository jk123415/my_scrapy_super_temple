# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# cookies dict 在这里处理
import random
import base64
import time
from selenium import webdriver
from scrapy import signals
from scrapy.exceptions import IgnoreRequest
from scrapy.http import HtmlResponse


class ScrapyTempleSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ScrapyTempleDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        # mongodb网址过滤
        url = request.url
        if spider.collection.find_one({'url': url}):
            spider.logger.info('已经采集过: %s' % url)
            raise IgnoreRequest
        else:
            return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class RandomUserAgent(object):
    def __init__(self, agents, cookies):
        # 使用初始化的agents列表
        self.agents = agents
        self.cookies = dict([x.split('=') for x in cookies.split('; ')])

    @classmethod
    def from_crawler(cls, crawler):
        # 获取settings的USER_AGENT列表并返回
        return cls(agents=crawler.settings.getlist('USER_AGENTS'),
                   cookies=crawler.settings.get('COOKIES_STR'))

    def process_request(self, request, spider):
        # 随机设置Request报头header的User-Agent
        request.headers.setdefault('User-Agent', random.choice(self.agents))
        request.cookies = self.cookies


# 代理服务器
proxyServer = "http://http-dyn.abuyun.com:9020"
# 代理隧道验证信息
proxyUser = "H01234567890123D"
proxyPass = "0123456789012345"
# for Python2
# proxyAuth = "Basic " + base64.b64encode(proxyUser + ":" + proxyPass)
# for Python3
proxyAuth = "Basic " + base64.urlsafe_b64encode(bytes((proxyUser + ":" + proxyPass), "ascii")).decode("utf8")


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        request.meta["proxy"] = proxyServer
        request.headers["Proxy-Authorization"] = proxyAuth


# selenium chrome 模拟请求
class SeleniumChorme(object):
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        self.chrome = webdriver.Remote('http://localhost:9515', desired_capabilities=options.to_capabilities())

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        url = request.url
        spider.logger.debug('chrome is Starting')
        self.chrome.get(url)
        time.sleep(1)
        return HtmlResponse(url=url, body=self.chrome.page_source, request=request, encoding='utf-8', status=200)
