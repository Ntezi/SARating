import scrapy


class ReviewItem(scrapy.Item):
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    date = scrapy.Field()
    user = scrapy.Field()
    title = scrapy.Field()
    review = scrapy.Field()
    stay_date = scrapy.Field()
