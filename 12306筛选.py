# -*- coding: utf-8 -*-
from splinter.browser import Browser
import time
import sys
import json
import urllib2
import ssl

browser = Browser('chrome')

local = {'changchun' : '长春,CCT',
         'yiwu' : '义乌,YWH',
         'shanghai' : '上海,SNH'
         }

class huoche :
    name = '*******'
    password = '********'
    startlocal = ''
    endlocal = ''
    datetime = ''
    loginurl = 'https://kyfw.12306.cn/otn/login/init'
    my12306url = 'https://kyfw.12306.cn/otn/index/initMy12306'
    xuanpiaourl = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
    #shaixuanurl = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + sys.argv[3] + '&leftTicketDTO.from_station='

    def __init__(self):
        browser.visit(self.loginurl)

    def denglu(self) :
        browser.find_by_id('username').fill(self.name)
        browser.find_by_id('password').fill(self.password)
        print u'请自行输入验证码...'
        while True :
            if browser.url != self.my12306url:
                time.sleep(1)
            else :
                break


    def xuanpiao(self) :
        browser.click_link_by_id('selectYuding')
        browser.cookies.add({'_jc_save_fromDate' : self.datetime})
        browser.cookies.add({'_jc_save_fromStation' : self.startlocal})
        browser.cookies.add({'_jc_save_toStation': self.endlocal})
        browser.reload()
        browser.click_link_by_id('query_ticket')
        # while (browser.is_element_not_present_by_text(u"预订")):
        #     browser.find_by_text(u"查询").click()
        #     time.sleep(3)
        # browser.find_by_text(u"预订")[0].click()
        # exit()
        # while browser.is_element_not_present_by_text(u'预订') :
        #     browser.click_link_by_id('query_ticket')
        #     time.sleep(3)
        # browser.find_by_text(u'预订')[0].click()
        # exit()

    def shaixuan(self) :
        while True :
            browser.reload()
            browser.click_link_by_id('query_ticket')
            ssl._create_default_https_context = ssl._create_unverified_context
            urll = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-02-21&leftTicketDTO.from_station=YWH&leftTicketDTO.to_station=SNH&purpose_codes=ADULT'
            req = urllib2.Request(urll)
            req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
            html = urllib2.urlopen(req).read()
            xinxi = json.loads(html)
            xinxi = xinxi['data']['result']
            lieche = {}
            n = 1
            # print u'以下列车还有车票...'
            for i in xinxi:
                shuju = i.split('|')
                if shuju[30] != u'无' or shuju[31] != u'无' or shuju[32] != u'无':
                    lieche[n] = {}
                    lieche[n][u'车号'] = shuju[3]
                    lieche[n][u'发车时间'] = shuju[8]
                    lieche[n][u'到站时间'] = shuju[9]
                    lieche[n][u'总历时'] = shuju[10]
                    lieche[n][u'无座'] = shuju[26]
                    lieche[n][u'硬卧'] = shuju[28]
                    lieche[n][u'硬座'] = shuju[29]
                    n += 1
            if lieche[1][u'硬卧'] != u'无' or lieche[2][u'硬卧'] != u'无':
                browser.find_by_text(u'预订')[0].click()
                browser.find_by_text(u'预订')[1].click()
                time.sleep(1)
                if browser.url != self.xuanpiaourl:
                    time.sleep(1)
                else :
                    break
            else :
                time.sleep(3)


    def dingpiao(self) :
        browser.click_link_by_id('normalPassenger_0')
        browser.click_link_by_id('submitOrder_id')
        exit()

if __name__ == '__main__' :
    huoche = huoche()
    # key1 = raw_input("Please input from station: ").decode(sys.stdin.encoding)
    # key2 = raw_input("Please input to station: ").decode(sys.stdin.encoding)
    huoche.startlocal = local[sys.argv[1]]
    huoche.endlocal = local[sys.argv[2]]
    huoche.datetime = sys.argv[3]
    huoche.denglu()
    huoche.xuanpiao()
    huoche.shaixuan()
    huoche.dingpiao()
