# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from fapka.items import PostItem
from bs4 import BeautifulSoup
import re
import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['4chan']
articles = db['posts']


class ToScrapeCSSSpider(scrapy.Spider):
    name = "4chan_thread_all"
    start_urls = [
        'http://boards.4channel.org/trv/thread/1541220',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, endpoint='render.html', args={'wait': 0.5})

    def parse(self, response):
        for div in response.css("div.post"):
            item = PostItem()

            item['author'] = BeautifulSoup(div.css(".name").extract_first()).get_text().strip()
            item['ts'] = BeautifulSoup(div.css(".dateTime::attr(data-utc)").extract_first()).get_text().strip()

            text = BeautifulSoup(div.css(".postMessage").extract_first()).get_text().strip()
            mentions = re.findall(r'>>(\d{7})', text)
            item['mentions'] = mentions
            text = re.sub(r'>>(\d{7})', "", text)
            text = re.sub(r'>', "", text)
            item['text'] = text

            id_string = BeautifulSoup(div.css(".postMessage::attr(id)").extract_first()).get_text().strip()
            item['id'] = re.sub(r"[^0-9]", "", id_string)

            post = {
                'id': item['id'],
                'author': item['author'],
                'ts': item['ts'],
                'mentions': item['mentions'],
                'text': item['text'],
                "created_at": datetime.datetime.utcnow()
            }
            articles.insert_one(post)

            yield item


