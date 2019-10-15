from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider, CrawlSpider, XMLFeedSpider, CSVFeedSpider
from scrapy.selector import Selector

from tour_crawler.items import EventItem
from tour_crawler.loaders import DefaultEventLoader, MetallicaEventLoader, SabatonEventLoader


class SabatonSpider(Spider):
    name = "sabaton_spider"
    custom_settings = {

    }
    start_urls = [
        'https://www.sabaton.net/tour/',
    ]

    def parse(self, response):
        shows_list = response.xpath("//div[@class='tour-wrapper']")
        for events_div in shows_list:
            event = SabatonEventLoader(selector=events_div)
            event.add_xpath('city', ".//div[@class='tour-location']/span/text()")
            event.add_xpath('country', ".//div[@class='tour-location']/span/text()")
            event.add_xpath('link', ".//a[@class='info button']//@href")
            event.add_xpath('venue', ".//div[@class='tour-details']/div[2]/text()")
            event.add_xpath('date', ".//div[@class='tour-date']/text()")
            event.add_xpath('tickets_link', ".//a[@title='Get tickets']//@href")
            event.load_item()
            yield event.item
