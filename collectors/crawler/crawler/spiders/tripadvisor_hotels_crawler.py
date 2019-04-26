# -*- coding: utf-8 -*-
import re

import scrapy

from crawler.review_item import ReviewItem

from crawler.UrlHelper import UrlHelper


class TripadvisorHotelsCrawlerSpider(scrapy.Spider):
    name = 'tripadvisor_hotels_crawler'
    allowed_domains = ['www.tripadvisor.com']
    urls = UrlHelper.hotel_urls
    # urls = UrlHelper.restaurant_urls
    # urls = UrlHelper.to_do_urls
    start_urls = urls

    def parse(self, response):
        url = response.url
        self.log('I just visited: ' + url)

        links = response.css('div.hotels-review-list-parts-ReviewTitle__reviewTitle--2Fauz > a::attr(href)').extract()

        if links:
            for link in links:
                link = response.urljoin(link)
                # yield {'link': link}
                yield scrapy.Request(url=link, callback=self.parse_review_details)

            # follow pagination link
            if not re.findall(r'or\d', url):
                next_page = re.sub(r'(-Reviews-)', r'\g<1>or5-', url)
            else:
                page_number = int(re.findall(r'or(\d+)-', url)[0])
                page_number_next = page_number + 5
                next_page = url.replace('or' + str(page_number), 'or' + str(page_number_next))
            yield scrapy.Request(next_page, meta={'dont_redirect': True}, callback=self.parse)

    def parse_review_details(self, response):
        review_item = ReviewItem()
        review_item['company_name'] = response.css('div.altHeadInline > a::text').extract_first()
        review_item['company_url'] = response.css('div.altHeadInline > a::attr(href)').extract_first()
        review_item['date'] = response.css('span.ratingDate::attr(title)').extract_first()
        review_item['user'] = response.css('div.info_text > div::text').extract_first()
        review_item['title'] = response.css('h1.title::text').extract_first()
        review_item['review'] = ' '.join(response.css('span.fullText::text').extract())
        review_item['stay_date'] = response.css('div.prw_reviews_stay_date_hsx::text').extract_first()
        yield review_item