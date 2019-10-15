from scrapy import Spider
from scrapy.loader import ItemLoader
from scrapy.spiders import SitemapSpider, CrawlSpider, XMLFeedSpider, CSVFeedSpider
from scrapy.selector import Selector

from tour_crawler.items import EventItem
from tour_crawler.loaders import DefaultEventLoader, MetallicaEventLoader


class MetallicaSpider(Spider):
    name = "metallica_spider"
    custom_settings = {

    }
    start_urls = [
        'https://www.metallica.com/tour/',
    ]

    def parse(self, response):
        # print(response.xpath('//title').get())
        # shows_list = response.xpath("//div[@class='shows-list shows-list--upcoming']")
        shows_list = response.xpath("//div[@class='show ']")
        # entering main loop with

        for events_div in shows_list:
            event = MetallicaEventLoader(selector=events_div)
            event.add_xpath('city', ".//a[@class='venue-city']//p[1]/text()")
            event.add_xpath('country', ".//a[@class='venue-city']//p[2]/text()")
            event.add_xpath('link', ".//a[@class='venue-city']//@href")
            event.add_xpath('venue', ".//p[@class='venue-name']/text()")
            event.add_xpath('date', "@data-show-id")
            event.add_xpath('tickets_link', ".//a[@title='Tickets']/@href")
            event.load_item()
            yield event.item


            # print(events_div.attrib['data-show-id'])
            # # print(events_div.attrib['data-show-id'])
            # # print(events_div.get())
            # all_events = events_div.xpath("@data-show-id").get()
            # print(all_events)
            # all_events_div = events_div.xpath(".//div[@class='ctas']//a")
            # print(all_events_div.get())
            # venue_city = events_div.xpath(".//a[@class='venue-city']").get()
            # print(venue_city)



            # print(all_events_div.getall())
            # print(all_events_div.xpath(".//div[@class='show-date-venue']").getall())
            # for event in all_events:
            #     print(event.get())
                # print(event.xpath("@data-show-id").get())
            # print(i.xpath("@data-show-id").get())
        # print(shows_list, type(shows_list))
        # print("--" * 99)
        # print(event.item)
        # yield
