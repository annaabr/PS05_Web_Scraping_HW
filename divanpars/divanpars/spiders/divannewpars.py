import scrapy
import csv

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/rostov-na-donu/category/svet"]

    # Инициализация списка для хранения данных
    # Инициализация списка для хранения данных
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'lamps.csv',
        'FEED_EXPORT_ENCODING': 'utf-8'  # Установка кодировки UTF-8
    }

    def parse(self, response):
        lamps = response.css('div._Ud0k')
        for lamp in lamps:
            yield {
                'name': lamp.css('div.lsooF span::text').get(),
                'price': lamp.css('div.pY3d2 span::text').get(),
                'url': lamp.css('a').attrib['href']
            }

