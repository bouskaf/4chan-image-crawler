# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest



class ToScrapeCSSSpider(scrapy.Spider):
    name = "idnes"
    start_urls = [
        'https://zpravy.idnes.cz/archiv.aspx?strana=%s' % page for page in range(1, 7491)
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):

        for div in response.css("div.art"):
            yield {
                'href': 'http:' + div.css("a::attr(href)").extract_first()
            }