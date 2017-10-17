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
    startDate = scrapy.Field()
    startDateTime = scrapy.Field()
    endDate = scrapy.Field()
    endDateTime = scrapy.Field()
    optionalCode = scrapy.Field()
    location = scrapy.Field()
    