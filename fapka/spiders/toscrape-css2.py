# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest



class ToScrapeCSSSpider(scrapy.Spider):
    name = "4chan2"
    start_urls = [
        'http://boards.4chan.org/s/thread/17526113',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):
        for image in response.css("a.fileThumb"):
            yield {
                'href': 'http:' + image.css("a::attr(href)").extract_first()
            }