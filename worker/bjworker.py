#!/usr/bin/python
#encoding=utf-8
import sys,re,urllib2,urllib,cookielib,chardet,time
from BeautifulSoup import BeautifulSoup
import sqlite3,json,datetime
from sys import argv
reload(sys)
sys.setdefaultencoding('utf8')
# by wangz
URLS={'ana_day': "http://bj.lianjia.com/fangjia/priceTrend/?analysis=1&duration=day",
     'ana_month' : "http://bj.lianjia.com/fangjia/priceTrend/?analysis=1",
     'fangjia':'http://bj.lianjia.com/fangjia/',
     'jianwei':'http://www.bjjs.gov.cn/bjjs/fwgl/fdcjy/fwjy/index.shtml'
    }
def add(vals):
    conn = sqlite3.connect('/root/git/ljdata/db.sqlite3') 
    curs=conn.cursor()
    query = 'INSERT INTO main_data (vtype,value,datetime,city,created_at) VALUES(?,?,?,?,?) '
    curs.execute(query,vals)
    conn.commit()
    conn.close()
def delete(vals):
    conn = sqlite3.connect('/root/git/ljdata/db.sqlite3')
    curs=conn.cursor()
    query = 'DELETE FROM main_data WHERE vtype=? and datetime=? and city=? '
    curs.execute(query,vals)
    conn.commit()
    conn.close()

def add_ms(vals):
    conn = sqlite3.connect('/root/git/ljdata/db.sqlite3')
    curs=conn.cursor()
    query = 'INSERT INTO main_msummary (value,datetime,city,created_at) VALUES(?,?,?,?) '
    curs.execute(query,vals)
    conn.commit()
    conn.close()

class Moofeel(object):
    def __init__(self):
        self.name = self.pwd = self.content = ''
        self.cj = cookielib.LWPCookieJar()
        try:
            self.cj.revert('moofeel.cookie')
        except Exception,e:
            print e
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
        urllib2.install_opener(self.opener)

    def get_r(self):

	req = urllib2.Request("http://bj.lianjia.com/ershoufang/")
	self.operate = self.opener.open(req)
	rawdata = self.operate.read()
	rawdata = rawdata.decode(chardet.detect(rawdata)['encoding'])
        for m in BeautifulSoup(rawdata).findAll('h2'):
            if m.get('class') == 'total fl':
		s = m.findAll('span')
		print s[0].string.strip()
		add(['r',int(s[0].string.strip()),time.strftime('%Y-%m-%d'),'bj',time.strftime('%Y-%m-%d %X')])
   
    def get_t_deal(self):

        req = urllib2.Request("http://bj.lianjia.com/chengjiao/")
        self.operate = self.opener.open(req)
        rawdata = self.operate.read()
        rawdata = rawdata.decode(chardet.detect(rawdata)['encoding'])
        for m in BeautifulSoup(rawdata).findAll('div'):
            if m.get('class') == 'total fl':
                s = m.findAll('span')
                print s[0].string.strip()
		#delete(['td',time.strftime('%Y-%m-%d'),'bj'])
                add(['td',int(s[0].string.strip()),time.strftime('%Y-%m-%d'),'bj',time.strftime('%Y-%m-%d %X')]) 


    def get_day_data(self):
        req = urllib2.Request(URLS.get("ana_day"))
        self.operate = self.opener.open(req)
        rawdata = self.operate.read()
        #rawdata = rawdata.decode(chardet.detect(rawdata)['encoding'])
        rawdata = rawdata.decode('unicode_escape')
 	print rawdata
	data = json.loads(rawdata)
	dt = data.get('time')

	dt = datetime.date(int(dt.get('year')),int(dt.get('month')[0:-1]),int(dt.get('day')[0:-1]))
        add(['nh',int(data.get('houseAmount')[-1]),dt,'bj',time.strftime('%Y-%m-%d %X')])
        add(['nc',int(data.get('customerAmount')[-1]),dt,'bj',time.strftime('%Y-%m-%d %X')])
        add(['ns',int(data.get('showAmount')[-1]),dt,'bj',time.strftime('%Y-%m-%d %X')])

    def get_month_data(self):
        req = urllib2.Request(URLS.get("ana_month"))
        self.operate = self.opener.open(req)
        rawdata = self.operate.read()
        #rawdata = rawdata.decode(chardet.detect(rawdata)['encoding'])
        rawdata = rawdata.decode('unicode_escape')
        print rawdata
        data = json.loads(rawdata)
        dt = data.get('time')

        dt = datetime.date(int(dt.get('year')),int(dt.get('month')[0:-1]),int(dt.get('day')[0:-1]))
        add(['mnh',int(data.get('houseAmount')[-1]),dt,'bj',time.strftime('%Y-%m-%d %X')])
        add(['mnc',int(data.get('customerAmount')[-1]),dt,'bj',time.strftime('%Y-%m-%d %X')])
        add(['mns',int(data.get('showAmount')[-1]),dt,'bj',time.strftime('%Y-%m-%d %X')])
	self.get_month_desc(dt)

    def get_month_desc(self,dt):
        req = urllib2.Request(URLS.get("fangjia"))
        self.operate = self.opener.open(req)
        rawdata = self.operate.read()
        rawdata = rawdata.decode(chardet.detect(rawdata)['encoding'])
        #rawdata = rawdata.decode('unicode_escape')
	#print rawdata
        for m in BeautifulSoup(rawdata).findAll('div'):
            if m.get('class') == 'txt hide':
		print m.text
		add_ms([m.text,dt,'bj',time.strftime('%Y-%m-%d %X')])

    def get_jianwei_data(self):
        req = urllib2.Request(URLS.get("jianwei"))
        self.operate = self.opener.open(req)
        rawdata = self.operate.read()
        rawdata = rawdata.decode(chardet.detect(rawdata)['encoding'])
        #rawdata = rawdata.decode('unicode_escape')
        #print rawdata
	bfsoup =  BeautifulSoup(rawdata)
	#i = 0#15,17
	for i,m in enumerate (bfsoup.findAll('table')):
            #if i == 15:
	    #	print m
	    if i == 17:
		value = m.findAll('td')[2].text
		dtstr = m.findAll('td')[0].text[0:-7]
  		dt = datetime.date(int(dtstr.split('-')[0]),int(dtstr.split('-')[1]),int(dtstr.split('-')[2]))
		add(['d',int(value),dt,'bj',time.strftime('%Y-%m-%d %X')])

if len(argv)>1:
    t = argv[1]
    m = Moofeel()
    if t == 'r':#总量
        m.get_r()
    if t== 'td':#总成交量
        m.get_t_deal()
    if t == 'ana_day':#每日的三个值
	m.get_day_data()
    if t == 'ana_mon':#每月的三个值
	m.get_month_data()
    if t == 'jw':
	m.get_jianwei_data()
