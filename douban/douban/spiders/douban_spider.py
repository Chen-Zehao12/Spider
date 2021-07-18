import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口rul，扔到调度器里面去
    start_urls = ['https://movie.douban.com/top250']

    # 默认解析方法
    def parse(self, response):
        # 循环电影的条目
        movie_list = response.xpath('//*[@id="content"]/div/div[1]/ol/li')
        for i_item in movie_list:
            # item文件导进来
            douban_item = DoubanItem()
            # 写详细的xpath，进行数据的解析
            douban_item['serial_number'] = i_item.xpath('./div[@class="item"]//em/text()').extract_first()
            douban_item['movie_name'] = i_item.xpath('./div[@class="item"]//span[@class="title"][1]/text()').extract_first()

            # 内容有换行，需要进行遍历处理
            content = i_item.xpath('./div[@class="item"]//div[@class="bd"]/p[1]/text()').extract()
            for i_content in content:
                content_s = "".join(i_content.split())
                douban_item['introduce'] = content_s

            douban_item['star'] = i_item.xpath('./div[@class="item"]//div[@class="bd"]/div[@class="star"]/span[2]/text()').extract_first()
            douban_item['evaluate'] = i_item.xpath('./div[@class="item"]//div[@class="bd"]/div[@class="star"]/span[4]/text()').extract_first()
            douban_item['describe'] = i_item.xpath('./div[@class="item"]//div[@class="bd"]/p[@class="quote"]/span/text()').extract_first()
            # 需要将数据yield到pipelines中
            yield douban_item

        # 解析下一页规则，取后页的xpath
        next_link = response.xpath('//span[@class="next"]/link/@href').extract()
        # 如果后页不为空，则进行
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250' + next_link, callback=self.parse)
