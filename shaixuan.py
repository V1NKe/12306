# -*- coding: utf-8 -*-
import urllib2
import ssl
import json
ssl._create_default_https_context = ssl._create_unverified_context
req = urllib2.Request('https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=2018-01-25&leftTicketDTO.from_station=HFH&leftTicketDTO.to_station=FZS&purpose_codes=ADULT')
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36')
html = urllib2.urlopen(req).read()
xinxi = json.loads(html)
xinxi = xinxi['data']['result']
lieche = {}
n = 1
print u'以下列车还有车票...'
for i in xinxi :
    shuju = i.split('|')
    if shuju[30] != u'无' or shuju[31] != u'无' or shuju[32] != u'无' :
        lieche[n] = {}
        lieche[n][u'车号'] = shuju[3]
        lieche[n][u'发车时间'] = shuju[8]
        lieche[n][u'到站时间'] = shuju[9]
        lieche[n][u'总历时'] = shuju[10]
        lieche[n][u'二等座'] = shuju[30]
        lieche[n][u'一等座'] = shuju[31]
        lieche[n][u'特等座'] = shuju[32]
        lieche[n][u'无座'] = shuju[26]
        lieche[n][u'硬座'] = shuju[27]
        lieche[n][u'软座'] = shuju[28]
        lieche[n][u'硬卧'] = shuju[29]
        n += 1
print json.dumps(lieche,ensure_ascii=False)