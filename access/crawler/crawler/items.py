# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class ReviewItem(scrapy.Item):
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    date = scrapy.Field()
    user = scrapy.Field()
    title = scrapy.Field()
    review = scrapy.Field()
    stay_date = scrapy.Field()


class HotelItem(scrapy.Item):
    name = scrapy.Field()
    url = scrapy.Field()
    category = scrapy.Field()
    location = scrapy.Field()
    address = scrapy.Field()
    star_ratings = scrapy.Field()
