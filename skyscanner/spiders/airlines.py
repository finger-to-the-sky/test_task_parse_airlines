import scrapy


class AirlinesSpider(scrapy.Spider):
    name = 'airlines'
    allowed_domains = ['skyscanner.com.ua']
    start_urls = ['http://skyscanner.com.ua/']

    def parse(self, response):
        pass
