# -*- coding: utf-8 -*-
import scrapy
import os

class StyleberrySpider(scrapy.Spider):
    name = "styleberry"
    start_urls = [
            'https://www.styleberry.co.kr/shop/shopdetail.html?branduid=' + str(i) for i in range(30000, 70000)
    ]
    def __init__(self):
        self.dirname = './styleberry/'
        if not os.path.exists(self.dirname): os.mkdir(self.dirname)

    def parse(self, response):
        uid = response.url[-5:]
        title = response.css("h3.tit-prd::text").extract_first()
        if title:
            dirname = self.dirname + uid + '_' + title + '/'
            if not os.path.exists(dirname): os.mkdir(dirname)
            for page in response.css("div.prd-detail center")[0].css("img::attr(src)").extract():
                filename = page.split('/')[-1]
                request = scrapy.Request(page, callback=self.jpg_write)
                request.meta['path'] = dirname + filename
                yield request

    def jpg_write(self, response):
        with open(response.meta['path'], 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % response.meta['path'])
