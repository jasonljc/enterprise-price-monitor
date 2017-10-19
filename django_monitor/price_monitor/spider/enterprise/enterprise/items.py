# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class EnterpriseItem(scrapy.Item):
    # define the fields for your item here like:
    searchTime = scrapy.Field()
    searchCriteria = scrapy.Field()
    startDateMonth = scrapy.Field()
    startDateInput = scrapy.Field()
    startDateTime = scrapy.Field()
    endDateMonth = scrapy.Field()
    endDateInput = scrapy.Field()
    endDateTime = scrapy.Field()
    optionalCode = scrapy.Field()
    location = scrapy.Field()
    car_class = scrapy.Field()
    car_price = scrapy.Field()
    car_total_price = scrapy.Field()
    