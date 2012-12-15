# -*- coding: utf-8 -*-
from grab.spider import Spider
from grab.spider import Task

from spiders.base import BaseHubSpider

class SimpleSpider(BaseHubSpider):
    initial_urls = ['http://www.utkonos.ru/cat/364', 'http://www.utkonos.ru/cat/384', 'http://www.utkonos.ru/cat/402']

    def task_initial(self, grab, task):
        pages = grab.xpath(".//div[@id='current']/div[5]/table/tr/td/div/a[@class='page last']/text()")
        print pages

        for page in range(1, int(pages) + 1):
            url = task.url + '/pg' + str(page) + '/'
            yield Task('page', url=grab.make_url_absolute(url))


    def task_page(self, grab, task):
        print 'PAGE url: %s' % task.url
        goods = grab.xpath_list(".//div[@id='current']/div[5]/div/table/tr/td/div/a[@class='name']")
        for product in goods:
            url = product.xpath(".//@href")[0]
            title = product.xpath(".//text()")[0].strip()
            yield Task('product', url=grab.make_url_absolute(url), title=title , page=task.url)


    def task_product(self, grab, task):
        print 'Product url: %s, title: %s' % (task.url, task.page)

        title  = grab.xpath(".//div[@id='current']/div/h1/text()")
        desc   = grab.xpath_text(".//div[@class='text']")
        weight = grab.xpath(".//div[@class='right_item_block']/div[@class='line']/div[2]/span/text()")
        price  = grab.xpath(".//div[@class='right_item_block']/div[@class='block first']/div/div[@class='price']/span[1]/text()")
        ext_id = grab.xpath(".//div[@class='right_item_block']/div[@class='line']/div[1]/span/text()")
        url    = task.url
        pict   = grab.make_url_absolute(grab.xpath(".//div[@id='current']/div/table/tr/td/span/a/@href"))


        data = dict(title=title, desc=desc, weight=weight, price=price, ext_id=ext_id, url=url, pict=pict)
#        print data

        self.save(data)
        self.log_progress(data['title'])
