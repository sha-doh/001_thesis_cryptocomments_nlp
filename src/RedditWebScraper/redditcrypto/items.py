# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

class CryptoItem(Item):
	title = Field()
	vote = Field()
	time = Field()
	comment = Field()

class CommentItem(Item):
	title = Field()
	subject = Field()
	comment = Field()
	votes = Field()
	time = Field()
	replies = Field()

# class RedditcryptoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
