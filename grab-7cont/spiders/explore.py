# -*- coding: utf-8 -*-
from spiders.base import BaseHubSpider
from grab.spider import Task

class StoreSpider(BaseHubSpider):
    initial_urls = ['http://corporate.7cont.ru/customers/shops/?region=None&shopFormat=None']

    def task_initial(self, grab, task):
        print '7Cont list of stores'

        stores = grab.xpath_list(".//*[@id='pagecontent_id']/div/table/tbody/tr")

        for store in stores:
            url = store.xpath(".//td[@class='name']/a/@href")[0]

            title = store.xpath("td[@class='name']/a/text()")[0].strip()

            address = store.xpath(".//td[@class='address']/text()")[1].strip()

            metro = store.xpath(".//td[@class='subway']/text()")[0].strip()

            yield Task('store', url=grab.make_url_absolute(url), title=title, metro=metro, address=address)

    def task_store(self, grab, task):
        print '7Cont store: %s' % task.url

        data = {'title': task.title, 'metro': task.metro, 'address': task.address}

        info = grab.xpath_list(".//*[@id='pagecontent_id']/div/div/div[@class='shopinfo']")
        for inf in info:
            if inf.xpath(".//span/text()")[0].strip().find(u'елефон') > 0:
                data['tel'] = inf.xpath(".//text()")[1]
            if inf.xpath(".//span/text()")[0].strip().find(u'работы') > 0:
                data['times'] = inf.xpath(".//text()")[1]

        self.save(data)
        self.log_progress(data['title'])
