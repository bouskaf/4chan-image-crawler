# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class FapkaItem(scrapy.Item):
    name = Field()
    image_urls = Field()
    images = Field()

class PostItem(scrapy.Item):
    author = Field()
    ts = Field()
    title = Field()
    text = Field()
    id = Field()
    mentions = Field()