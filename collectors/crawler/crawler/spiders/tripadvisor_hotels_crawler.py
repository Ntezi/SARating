# -*- coding: utf-8 -*-
import re

import scrapy

from crawler.items import ReviewItem, HotelItem


class TripadvisorHotelsCrawlerSpider(scrapy.Spider):
    name = 'tripadvisor_hotels_crawler'
    allowed_domains = ['www.tripadvisor.com']

    urls = [
        'https://www.tripadvisor.com/Hotels-g3685401-Northern_Province-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g3685404-Western_Province-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g3685403-Southern_Province-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g3685402-Eastern_Province-Hotels.html',
        'https://www.tripadvisor.com/Hotels-g293829-Kigali_Kigali_Province-Hotels.html'
    ]
    start_urls = urls

    def parse(self, response):

        for listing in response.css('div.listing'):
            name = listing.css('div.listing_title > a::text').extract_first()
            url = listing.css('a.property_title::attr(href)').extract_first()
            category = "Hotel"
            location = response.css('li.breadcrumb > a.link > span::text').extract()[2]

            hotel_link = response.urljoin(url)
            request = scrapy.Request(hotel_link, callback=self.parse_hotel_details)

            request.meta['name'] = name
            request.meta['url'] = url
            request.meta['category'] = category
            request.meta['location'] = location

            yield request

        # follow pagination link
        url = response.url
        if not re.findall(r'oa\d+', url):

            next_page = ''
            if '-g3685401-' in url:
                next_page = re.sub(r'(-g3685401-)', r'\g<1>oa30-', url)
            elif '-g3685402-' in url:
                next_page = re.sub(r'(-g3685402-)', r'\g<1>oa30-', url)
            elif '-g3685403-' in url:
                next_page = re.sub(r'(-g3685403-)', r'\g<1>oa30-', url)
            elif '-g3685404-' in url:
                next_page = re.sub(r'(-g3685404-)', r'\g<1>oa30-', url)
            elif '-g293829-' in url:
                next_page = re.sub(r'(-g293829-)', r'\g<1>oa30-', url)
        else:
            page_number = int(re.findall(r'oa(\d+)-', url)[0])
            page_number_next = page_number + 30
            next_page = url.replace('oa' + str(page_number), 'oa' + str(page_number_next))
        yield scrapy.Request(next_page, meta={'dont_redirect': True}, callback=self.parse)

    def parse_hotel_details(self, response):

        # ********************************* Hotel Details ********************************************
        # To get hotel details, comment lines below before uncomment : yield hotel_item
        # hotel_item = HotelItem()
        # # hotel_item['name'] = response.meta['name']
        # hotel_item['name'] = response.css('h1.ui_header::text').extract_first()
        # hotel_item['url'] = response.meta['url']
        # hotel_item['category'] = response.meta['category']
        # hotel_item['location'] = response.meta['location']
        # hotel_item['address'] = response.css('span.street-address::text').extract_first()
        # hotel_item['star_ratings'] = response.css(
        #     'div.hotels-hotel-review-about-with-photos-Reviews__rating--2X_zZ > span::text').extract_first()
        # yield hotel_item

        # **************************** Review Details *************************************************
        # To get review details, comment line "yield hotel_item" above before running

        review_links = response.css(
            'div.hotels-review-list-parts-ReviewTitle__reviewTitle--2Fauz > a::attr(href)').extract()

        if review_links:
            for link in review_links:
                link = response.urljoin(link)
                # yield {'link': link}
                yield scrapy.Request(url=link, callback=self.parse_review_details)

            # follow pagination link
            url = response.url
            self.log('Hotel URL: ' + response.url)
            if not re.findall(r'or\d', url):
                next_page = re.sub(r'(-Reviews-)', r'\g<1>or5-', url)
            else:
                page_number = int(re.findall(r'or(\d+)-', url)[0])
                page_number_next = page_number + 5
                next_page = url.replace('or' + str(page_number), 'or' + str(page_number_next))
            yield scrapy.Request(next_page, meta={'dont_redirect': True}, callback=self.parse_hotel_details)

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
