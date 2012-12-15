# -*- coding: utf-8 -*-
from grab.spider import Spider
from grab.spider import Task

from spiders.base import BaseHubSpider

class SimpleSpider(BaseHubSpider):
    initial_urls = ['http://www.mgnl.ru/customers/address/list/']

    def task_initial(self, grab, task):
        stores = grab.xpath_list(".//div[@id='tab_cont_0']/table/tr/td/dl/dd/a")

        for store in stores:
            url = store.xpath(".//@href")[0]
            title = store.xpath(".//text()")[0].strip()
            yield Task('store', url=grab.make_url_absolute(url), title=title)

    def task_store(self, grab, task):
        print 'Magn store: %s' % task.url

        address = grab.xpath_text(".//*[@id='card_right']/h1")

        times   = grab.xpath(".//*[@id='card_right']/table/tr/td[@class='time']/text()")

        if grab.xpath_exists(".//*[@id='card_right']/table/tr/td[@class='phone']/nobr"):
            tel     = grab.xpath_text(".//*[@id='card_right']/table/tr/td[@class='phone']/nobr")
        else:
            tel = u""

        if grab.xpath_exists(".//*[@id='card_right']/table/tr/td[@class='metro']"):
            city  = u"Москва"
            metro = grab.xpath_text(".//*[@id='card_right']/table/tr/td[@class='metro']")
        else:
            city  = u""
            metro = u""



        data = dict(title=u"Магнолия", city=city, metro=metro, address=address, tel=tel, times=times)
        print data

        self.save(data)
        self.log_progress(data['title'])
