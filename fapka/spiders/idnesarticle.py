# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from bs4 import BeautifulSoup


class ToScrapeCSSSpider(scrapy.Spider):
    name = "idnesarticle"
    start_urls = [
        'https://zpravy.idnes.cz/stocena-auta-tachometr-pretoceny-ojeta-auta-podvod-fxm-/domaci.aspx?c=A180920_094019_domaci_kuce'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse,
                                endpoint='render.html',
                                args={'wait': 0.5},
                                )

    def parse(self, response):

        opener = response.css("div.opener").extract_first()
        text = response.css("#art-text").extract_first()
        disc_nr = response.css("#moot-linkin span").extract_first()
        disc_span = response.css("#moot-linkin")


        disc_url = disc_span.css("a::attr(href)").extract_first()
        disc_url = "https://zpravy.idnes.cz" + disc_url + "&razeni=time"



        authors = response.css("div.authors").extract_first()

        disc_nr = [int(s) for s in list(disc_nr) if s.isdigit()]

        disc_nr = int("".join(map(str, disc_nr)))



        opener_text = BeautifulSoup(opener).get_text().strip()
        opener_text = str(opener_text)
        text_text = BeautifulSoup(text).get_text().strip()

        authors_text = BeautifulSoup(authors).get_text().strip()
        yield {
            'opener': opener_text,
            #'text': text_text,
            'authors': authors_text,
            'disc_nr': disc_nr,
            'discussion_url': disc_url
        }