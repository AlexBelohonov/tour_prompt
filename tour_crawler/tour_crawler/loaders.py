from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, Compose, MapCompose

from tour_crawler.items import EventItem


class MapRstrip:
    """

    """
    def __call__(self, values, *args, **kwargs):
        return [value.rstrip(',') for value in values]


class GetFirstTen:
    """

    """
    def __call__(self, values, *args, **kwargs):
        return [value[:10] for value in values]


class DefaultEventLoader(ItemLoader):
    default_item_class = EventItem
    default_output_processor = TakeFirst()


class MetallicaEventLoader(DefaultEventLoader):
    date_in = GetFirstTen()
    city_in = MapRstrip()


class SabatonEventLoader(DefaultEventLoader):
    city_in = MapCompose(lambda v: v.split(',')[0])
    country_in = MapCompose(lambda v: v.split(',')[1])
