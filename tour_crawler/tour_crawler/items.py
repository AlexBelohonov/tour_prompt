# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TourCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class EventItem(scrapy.Item):
    city = scrapy.Field()
    country = scrapy.Field()
    venue = scrapy.Field()
    date = scrapy.Field()
    link = scrapy.Field()
    tickets_link = scrapy.Field()
