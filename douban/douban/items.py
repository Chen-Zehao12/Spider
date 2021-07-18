# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    serial_number = scrapy.Field()  # 电影序号
    movie_name = scrapy.Field()     # 电影名称
    introduce = scrapy.Field()      # 电影介绍
    star = scrapy.Field()           # 电影星级
    evaluate = scrapy.Field()       # 电影评论数
    describe = scrapy.Field()       # 电影描述
