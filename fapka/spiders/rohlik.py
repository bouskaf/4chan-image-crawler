# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup
import datetime
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['rohlik']
products = db['products']


class ToScrapeCSSSpider(scrapy.Spider):
    name = "rohlik"
    start_urls = [
        'https://www.rohlik.cz/c300101000-pekarna-a-cukrarna'
    ]





    def start_requests(self):
        script = """function main(splash)
                            local num_scrolls = 5
                            local scroll_delay = 1.0

                            local scroll_to = splash:jsfunc("window.scrollTo")
                            local get_body_height = splash:jsfunc(
                                "function() {return document.body.scrollHeight;}"
                            )
                            assert(splash:go(splash.args.url))
                            splash:wait(splash.args.wait)

                            for _ = 1, num_scrolls do
                                scroll_to(0, get_body_height())
                                splash:wait(scroll_delay)
                            end        
                            return splash:html()
                        end"""
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='execute',
                                args={'wait': 0.5, 'lua_source': script},
                                )

    def parse(self, response):
        for div in response.css("div.item"):
            price = div.css("span.productCard__price").extract_first()
            name = div.css(".productCard__title").extract_first()
            url = div.css("a.productCard__product::attr(href)").extract_first()
            image_url = div.css(".productCard__imageWrapper img::attr(src)").extract_first()

            price_text = ''
            if(price):
                price_text = BeautifulSoup(price).get_text().strip()
                price_text = [int(s) for s in list(price_text) if s.isdigit()]
                price_text = (int("".join(map(str, price_text)))) / 100
            name_text = ''
            if(name):
                name_text = BeautifulSoup(name).get_text().strip()

            product = {
                "price": {
                    "price": price_text,
                    "price_per_kg": "TBD"
                },
                "name": name_text,
                "url": url,
                "image_url": image_url,
                "created_at": datetime.datetime.utcnow()
            }
            products.insert_one(product)

            yield {
                'name': name_text,
                'price': price_text,
                'url': url,
                'image_url': image_url
            }