import scrapy
from liepin.items import LiepinItem


class LpSpider(scrapy.Spider):
    name = 'lp'
    allowed_domains = ['liepin.com']
    start_urls = ['https://www.liepin.com/zhaopin/']

    def parse(self, response, **kwargs):
        item = LiepinItem()
        title = response.xpath('//div[@class=\'job-info\']/h3/@title').extract()
        item['title'] = title
        return item
