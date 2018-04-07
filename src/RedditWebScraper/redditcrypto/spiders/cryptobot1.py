# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from redditcrypto.items import CommentItem


class Cryptobot1Spider(CrawlSpider):
    name = 'cryptobot1'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/r/CryptoCurrency/']

    rules = [
    	# Rule(LinkExtractor(
    	# 	allow=['/r/CryptoCurrency/\?count=\d*&after=\w*']),
    	# 	callback='parse_item',
    	# 	follow=True)

    	Rule(LinkExtractor(
    		allow=['/r/CryptoCurrency/comments/\w*']),
    		callback='parse_comments',
    		follow=True)
    ]

    # def parse_item(self, response):

    # 	selector_list = response.css('div.thing')

    # 	for selector in selector_list:
    # 		item = CryptoItem()
    # 		item['title'] = selector.css('.title.may-blank::text').extract()
    # 		item['vote'] = selector.css('.score.unvoted::text').extract()
    # 		item['time'] = selector.css('time::attr(datetime)').extract()
    # 		item['comment'] = selector.css('.comments::text').extract()

    # 		yield item

    def parse_comments(self, response):

    	selector_list = response.xpath('//div[@data-type="comment"]')

    	for selector in selector_list:
    		item = CommentItem()
    		item['title'] = response.css('.title.may-blank::text').extract()
    		item['subject'] = response.css('.linkflairlabel::text').extract()
    		item['comment'] = selector.xpath('normalize-space(.//form/div/div)').extract()
    		item['votes'] = selector.xpath('div/p/span[contains(@class, "score unvoted")]/text()').extract()
    		item['time'] = selector.xpath('div/p/time/@datetime').extract()
    		item['replies'] = selector.xpath('@data-replies').extract()

    		yield item