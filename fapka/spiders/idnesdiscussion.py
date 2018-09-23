# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup


class ToScrapeCSSSpider(scrapy.Spider):
    name = "idnesdisc"
    start_urls = [
        'https://zpravy.idnes.cz/diskuse.aspx/?iddiskuse=A180920_094019_domaci_kuce'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):

        for div in response.css("div.contribution"):
            text = div.css("td.cell div.user-text").extract_first()
            name = div.css("td.cell .name a").extract_first()
            rating = div.css("td.cell div.score").extract_first()

            text_text = BeautifulSoup(text).get_text().strip()
            name_text = BeautifulSoup(name).get_text().strip()
            name_text = ''.join([i for i in name_text if not i.isdigit()])
            rating_text = BeautifulSoup(rating).get_text().strip()


            yield {
                'text':  text_text,
                'name':  name_text,
                'rating': rating_text
            }