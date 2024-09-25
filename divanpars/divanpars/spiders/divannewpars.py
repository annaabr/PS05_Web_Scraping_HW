import scrapy


class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/rostov-na-donu/category/svet"]

    def parse(self, response):
        lamps = response.css('div._Ud0k')
        for lamp in lamps:
            yield {
                'name' : lamp.css('div.lsooF span::text').get(),
                'price' : lamp.css('div.pY3d2 span::text').get(),
                'url' : lamp.css('a').attrib['href']
            }

