# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    gdp = scrapy.Field()
    gdp_per_capital = scrapy.Field()
    unemployment_rate = scrapy.Field()
    dollar_per_day = scrapy.Field()
    population = scrapy.Field()
    population_density = scrapy.Field()
    land_area = scrapy.Field()
    early_marriages = scrapy.Field()
    literacy_rate = scrapy.Field()
    
