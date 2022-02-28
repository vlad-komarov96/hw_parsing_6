import scrapy


class JobParserItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    name = scrapy.Field()
    salary = scrapy.Field()
    vacancy_link = scrapy.Field()
    site_scraping = scrapy.Field()