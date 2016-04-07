# -*- coding: utf-8 -*-
#encoding:utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import redis
from crawler import Zhihu_Crawler

#connect to redis server
red=redis.Redis(host='localhost', port=6379, db=1)


def check_url(url):
    if red.sadd("url_crawled",url):
        red.lpush("url_queue",url)


if __main__=="__name__":
    i=0
    red.lpush("url_queue","")
    while(url=red.lpop("url_queue")):
        i=i+1
        new_crawler=Zhihu_Crawler(url)
        new_crawler.send_request()
        if (i==100):
            break