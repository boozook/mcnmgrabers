# -*- coding: utf-8 -*-
from spiders.base import BaseHubSpider
from grab.spider import Task
import json
from funcy import cat

MOSCOW_STORES = [
             {"name" : u"Ашан"                 , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498342592', "count": 1},
             {"name" : u"Ашан Сити"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136499245829', "count": 1},
             {"name" : u"Бахетле"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498442634', "count": 1},
             {"name" : u"Fix Price"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498284443', "count": 7},
             {"name" : u"Перекресток"          , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498303078', "count": 9},
             {"name" : u"Пятерочка"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498316193', "count": 22},
             {"name" : u"Пятерочка"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504137598373049', "count": 11},
             {"name" : u"Виктория"             , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498300771', "count": 2},
             {"name" : u"Дикси"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498313374', "count": 16},
             {"name" : u"Азбука вкуса"         , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498318829', "count": 3},
             {"name" : u"BILLA"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498300984', "count": 4},
             {"name" : u"Седьмой Континент"    , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498305253', "count": 7},
             {"name" : u"Оливье"               , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498657788', "count": 1},
             {"name" : u"Вкус Вилл"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504137598285175', "count": 1},
             {"name" : u"Магнит"               , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498517723', "count": 4},
             {"name" : u"Магнолия"             , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498318542', "count": 9},
             {"name" : u"Spar"                 , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498498930', "count": 1},
             {"name" : u"АЛМИ"                 , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498312720', "count": 2},
             {"name" : u"Атак"                 , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498319427', "count": 3},
             {"name" : u"Зеленый перекресток"  , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498782611', "count": 1},
             {"name" : u"Копейка"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498316695', "count": 1},
             {"name" : u"Мой магазин"          , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498632232', "count": 1},
             {"name" : u"Минутамаркет"         , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504137598314451', "count": 3},
             {"name" : u"Я любимый"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136499567481', "count": 1},
             {"name" : u"Перекресток Экспресс" , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136499183457', "count": 3},
             {"name" : u"Ситистор"             , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498391760', "count": 1},
             {"name" : u"АБК"                  , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498319201', "count": 2},
             {"name" : u"Алые Паруса"          , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498318968', "count": 1},
             {"name" : u"Е.Д.А."               , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498313473', "count": 1},
             {"name" : u"ГастроноМир"          , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498865772', "count": 1},
             {"name" : u"Диксика"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498442803', "count": 2},
             {"name" : u"Авоська"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498316240', "count": 3},
             {"name" : u"Покупай"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498526083', "count": 1},
             {"name" : u"Едофф"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504137598312613', "count": 1},
             {"name" : u"Манго"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136499127858', "count": 1},
             {"name" : u"Рось"                 , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498619782', "count": 1},
             {"name" : u"Сахарный Лев"         , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498725159', "count": 1},
             {"name" : u"7Я"                   , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498388752', "count": 1},
             {"name" : u"Город изобилия"       , "url" : 'http://demo.api.2gis.ru/filials?firm_id=4504136498322806', "count": 1}
         ]

NOVGOROD_STORES = [
             {"name" : u"Магнит"               , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474280915', "count": 1},
             {"name" : u"Пятёрочка"            , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474275202', "count": 1},
             {"name" : u"Дикси"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474283812', "count": 1},
             {"name" : u"Осень"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474275788', "count": 1},
             {"name" : u"Вольный купец"        , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474277932', "count": 1},
             {"name" : u"Полушка"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474278695', "count": 1},
             {"name" : u"Народная 7Я семьЯ"    , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474283727', "count": 1},
             {"name" : u"Квартал"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474287603', "count": 1},
             {"name" : u"Тележка"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474288457', "count": 1},
             {"name" : u"Адепт"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474285862', "count": 1},
             {"name" : u"Околица"              , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474287801', "count": 1},
             {"name" : u"Велес"                , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474286393', "count": 1},
             {"name" : u"Август"               , "url" : 'http://demo.api.2gis.ru/filials?firm_id=10837323474285684', "count": 1}
         ]

class StoreSpider(BaseHubSpider):

    initial_urls = cat([ [s["url"] + "&page=" + str(i) for i in range(1, int(s["count"]) + 1, 1)] for s in NOVGOROD_STORES])

    def task_initial(self, grab, task):

        store_urls = grab.xpath_list(".//*[@id='selectable-content']/div/div/div/ol/li/h2/a/@href")

        for url in store_urls:
            yield Task('store', url=grab.make_url_absolute(url))

    def task_store(self, grab, task):
        print '7Cont store: %s' % task.url

        full_name = grab.xpath(".//*[@id='selectable-content']/div/div/h1/text()").split(",")
        if len(full_name) == 1:
            title  = full_name[0]
            kind = ""
        else:
            title  = full_name[0]
            kind = full_name[1]

        if not grab.xpath_exists(".//ul[@class='address-info']/li[2]/text()"):
            return

        location = grab.xpath(".//ul[@class='address-info']/li[2]/text()").replace(u"(Координаты: ","").replace(u")","").split(" ")

        lat=location[0]
        lon=location[1]


        phones = []
        for phone in grab.xpath_list(".//ul[@class='phone-info']/li"):
            p = phone.xpath(".//text()")
            if len(p) == 1:
                tel = p[0].strip()
                comment = ""
            elif len(p) == 2:
                tel = p[0].strip()
                comment = p[1].strip().replace(u"- ","")


            phones.append(dict(tel=tel,comment=comment))

        webs = []
        for info in grab.xpath_list(".//ul[@class='web-info']/li"):
            p = info.xpath(".//a/text()")[0]
            webs.append(p)
            print p

        if grab.xpath_exists(".//span[@class='dg-firm-schedule-24']"):
            week_schedule = "24/7"
        else:
            week_schedule = []
            for day_schedule in grab.xpath_list(".//span[@class='dg-label']/text()"):
                s = day_schedule.split(u"–")
                week_schedule.append({"from":s[0],"to":s[1]})
        print week_schedule

        pay_methods = grab.xpath_list(".//ul[@class='dg-api-firm-attrs']/li/span/text()")

        data = dict(title=title, kind=kind, lat=lat, lon=lon, phones=json.dumps(phones), webinfo=json.dumps(webs), schedule=json.dumps(week_schedule), pay=json.dumps(pay_methods))
        self.save(data)
        self.log_progress(str(lat) + " " +str(lon) )
