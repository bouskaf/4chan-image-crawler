# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest



class ToScrapeCSSSpider(scrapy.Spider):
    name = "4chan_catalog"
    start_urls = [
        'http://boards.4chan.org/s/catalog',
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_catalog,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse_catalog(self, response):
        for thread in response.css("div.thread"):
            url = 'http:' + thread.css("a::attr(href)").extract_first()

            type = 1
            if type == 0:
                yield SplashRequest(url, self.parse_thread,
                                    endpoint='render.html',
                                    args={'wait': 0.5},
                                    )
            else:
                name = thread.css(".teaser b::text").extract_first()

                yield {
                    'href': 'http:' + thread.css("a::attr(href)").extract_first(),
                    'title':  thread.css(".teaser b::text").extract_first(),
                    'teaser': thread.css(".teaser::text").extract_first()
                }

    def parse_thread(self, response):
        for image in response.css("a.fileThumb"):
            yield {
                'href': 'http:' + image.css("a::attr(href)").extract_first()
            }