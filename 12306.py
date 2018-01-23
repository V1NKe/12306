# -*- coding: utf-8 -*-
from splinter.browser import Browser
import time
import sys
import requests
import json

browser = Browser('chrome')

local = {'changchun' : '长春,CCT',
         'yiwu' : '义乌,YWH'
         }

class huoche :
    name = '***'
    password = '********'
    startlocal = ''
    endlocal = ''
    datetime = ''
    loginurl = 'https://kyfw.12306.cn/otn/login/init'
    my12306url = 'https://kyfw.12306.cn/otn/index/initMy12306'
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
        while browser.is_element_not_present_by_text(u'预订') :
            browser.click_link_by_id('query_ticket')
            time.sleep(3)
        browser.find_by_text(u'预订')[0].click()
        exit()

    # def shaixuan(self) :


if __name__ == '__main__' :
    huoche = huoche()
    # key1 = raw_input("Please input from station: ").decode(sys.stdin.encoding)
    # key2 = raw_input("Please input to station: ").decode(sys.stdin.encoding)
    huoche.startlocal = local[sys.argv[1]]
    huoche.endlocal = local[sys.argv[2]]
    huoche.datetime = sys.argv[3]
    huoche.denglu()
    huoche.xuanpiao()
    # huoche.shaixuan()
