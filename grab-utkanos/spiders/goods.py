# -*- coding: utf-8 -*-
"""
Crawl goods form Utkonos
"""
from grab.spider import Spider
from grab.spider import Task

from spiders.base import BaseHubSpider

class GoodsSpider(BaseHubSpider):
    initial_urls = ['http://www.utkonos.ru/cat/1']

    def task_initial(self, grab, task):
#        print 'Utkonos list of categories'


        cats = grab.xpath_list(".//div[@id='current']/div/div/a")

#        print "cats= " + str(len(cats))
        for category in cats:
            url = category.xpath(".//@href")[0]
            title = category.xpath(".//text()")[0].strip()

            yield Task('category', url=grab.make_url_absolute(url)+'chp4', title=title)

    def task_category(self, grab, task):
#        print 'Category url: %s, title: %s' % (task.url, task.title)

        # если есть снова подкатегории то снова сюда
        categories = grab.xpath_list(".//div[@id='current']/div/h2/a")
        if categories:
            for category in categories:
                url = category.xpath(".//@href")[0]
                title = category.xpath(".//text()")[0].strip()
                yield Task('category', url=grab.make_url_absolute(url)+'chp4', title=title)

        else:
            goods = grab.xpath_list(".//div[@id='current']/div[5]/div/table/tr/td/div/a[@class='name']")
            if goods:

                for product in goods:
                    url = product.xpath(".//@href")[0]
                    title = product.xpath(".//text()")[0].strip()
                    print grab.make_url_absolute(url)

#                    yield Task('product', url=grab.make_url_absolute(url), title=title)

    '''
    def task_subcategory(self, grab, task):
#        print 'Sub Category url: %s, title: %s' % (task.url, task.subcat_title)
        goods = grab.xpath_list(".//div[@id='current']/div[5]/div/table/tr/td/div/a[@class='name']")

        if goods:
#            print "goods=%s in %s" % (str(len(goods)), task.subcat_title)
            for product in goods:
                url = product.xpath(".//@href")[0]
                title = product.xpath(".//text()")[0].strip()
#               print url
                yield Task('product', url=grab.make_url_absolute(url), title=title, cat_title=task.cat_title, subcat_title=task.subcat_title)
    '''

    def task_product(self, grab, task):
#        print 'Product url: %s, title: %s, cat: %s, subcat: %s' % (task.url, task.title, task.cat_title, task.subcat_title)

        title  = grab.xpath(".//div[@id='current']/h1")
        desc   = grab.xpath(".//div[@id='current']/div[4]/div/div/text()")
        weight = grab.xpath(".//div[@id='current']/div[4]/table/tr/td/div/div/div[2]/span/text()")
        price  = grab.xpath(".//div[@id='current']/div[4]/table/tr/td/div/div/div/div/span[1]/text()")
        ext_id = grab.xpath(".//div[@id='current']/div[4]/table/tr/td/div/div/div/span/text()")
#        cat    = task.cat_title
#        subcat = task.subcat_title
        url    = task.url
        pict   = grab.xpath(".//div[@id='current']/div/table/tr/td/span/a/@href")

#        data = dict(title=title, desc=desc, weight=weight, price=price, ext_id=ext_id, cat=cat, subcat=subcat, url=url, pict=pict)
        data = dict(title=title, desc=desc, weight=weight, price=price, ext_id=ext_id, url=url, pict=pict)
        print data

        self.save(data)
        self.log_progress(data['title'])
