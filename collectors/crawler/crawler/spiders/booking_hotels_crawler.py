# -*- coding: utf-8 -*-
import scrapy
from crawler.review_item import ReviewItem

# crawl up to 6 pages of review per hotel
max_pages_per_hotel = 6

class BookingHotelsCrawlerSpider(scrapy.Spider):
    name = 'booking_hotels_crawler'
    # allowed_domains = ['booking.com']
    start_urls = ["https://www.booking.com/searchresults.html?city=-2181358"]

    pageNumber = 1

    # for every hotel
    def parse(self, response):
        hotel_urls = response.css('h3.sr-hotel__title > a::attr(href)').extract()
        for hotel_url in hotel_urls:
            hotel_link_ = hotel_url.replace('\n/', '')
            hotel_link__ = hotel_link_.replace('?from=searchresults\n#hotelTmpl', '')
            hotel_link = response.urljoin(hotel_link__)
            request = scrapy.Request(hotel_link, callback=self.parse_hotel)
            request.meta['hotel_link'] = hotel_link
            yield request

        next_page = response.css('li.bui-pagination__next-arrow > a::attr(href)').extract_first()
        if next_page:
            hotel_link = response.urljoin(next_page)
            yield scrapy.Request(hotel_link, self.parse)

    # get its reviews page
    def parse_hotel(self, response):
        review_urls = response.css('div.hotel_reviews_url > a::attr(href)').extract_first()
        review_link = response.urljoin(review_urls)
        hotel_link = response.meta['hotel_link']
        request = scrapy.Request(review_link, callback=self.parse_reviews)
        request.meta['hotel_link'] = hotel_link
        return request

    # and parse the reviews
    def parse_reviews(self, response):
        url = response.url
        self.log('I just visited: ' + url)

        for post in response.css('li.review_item'):
            review_item = ReviewItem()

            review_item_date_ = post.css('p.review_item_date::text').extract_first()
            review_item_date__ = review_item_date_.replace('\nReviewed: ', '')
            review_item_date = review_item_date__.replace('\n', '')

            review_stay_date_ = post.css('p.review_staydate::text').extract_first()
            review_stay_date__ = review_stay_date_.replace('\nStayed in ', '')
            review_stay_date = review_stay_date__.replace('\n', '')

            review_neg = post.css('p.review_neg > span::text').extract_first()
            review_pos = post.css('p.review_pos > span::text').extract_first()
            review = "{} {}".format(review_neg, review_pos)

            review_item['company_name'] = response.css('h1.hotel_name > a::text').extract_first()
            review_item['company_url'] = response.meta['hotel_link']
            review_item['date'] = review_item_date
            review_item['user'] = post.css('p.reviewer_name > span::text').extract_first()
            review_item['title'] = post.css('div.review_item_header_content > span::text').extract_first()
            review_item['review'] = review
            review_item['stay_date'] = review_stay_date
            yield review_item

        next_page = response.css('p.review_next_page > a::attr(href)').extract_first()
        if next_page:
            url = response.urljoin(next_page)
            yield scrapy.Request(url, self.parse_reviews)
