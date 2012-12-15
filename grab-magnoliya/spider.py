# -*- coding: utf-8 -*-

from random import randint
from grab import Grab
from grab.spider import Spider, Task
from grab.tools.logs import default_logging

from spiders.simple import SimpleSpider

from config import default_spider_params, Session


def my_headers():
    return {
        'Accept': 'text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.%d' % randint(2, 5),
        'Accept-Language': 'ru-ru,ru;q=0.%d' % (randint(5, 9)),
        'Accept-Charset': 'utf-8,windows-1251;q=0.7,*;q=0.%d' % randint(5, 7),
        'Keep-Alive': '300',
        'Expect': '',
    }

if __name__ == '__main__':
    default_logging()

    bot = SimpleSpider(**default_spider_params())
    bot.setup_grab(timeout=4096, connect_timeout=10, headers=my_headers())

    bot.run()
    print bot.render_stats()
