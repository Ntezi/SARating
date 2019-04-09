import scrapy


class ListingItem(scrapy.Item):
    name = scrapy.Field()
    reviews = scrapy.Field()