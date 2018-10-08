# # -*- coding: utf-8 -*-
# import scrapy
# from scrapy_splash import SplashRequest
# import pymysql
#
# connection = pymysql.connect(host='localhost',
#                              port=8890,
#                              user='root',
#                              password='root',
#                              db='idnes',
#                              charset='utf8mb4',
#                              cursorclass=pymysql.cursors.DictCursor)
#
#
#
# class ToScrapeCSSSpider(scrapy.Spider):
#     name = "idnes_sql"
#     start_urls = [
#         'https://zpravy.idnes.cz/archiv.aspx?strana=%s' % page for page in range(0, 10)
#     ]
#
#
#
#
#     def write_db(self, url):
#         with connection.cursor() as cursor:
#             sql = "INSERT INTO `articles` (`url`) VALUES (%s)"
#             cursor.execute(sql, url)
#
#
#
#     def start_requests(self):
#         for url in self.start_urls:
#             yield SplashRequest(url, self.parse,
#                                 endpoint='render.html',
#                                 args={'wait': 0.5},
#                                 )
#
#     def parse(self, response):
#
#         for div in response.css("div.art"):
#             url = str(div.css("a::attr(href)").extract_first())
#             self.write_db(url)
#
#         connection.commit()
