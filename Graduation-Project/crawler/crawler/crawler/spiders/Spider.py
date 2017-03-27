# coding:utf-8

import scrapy
import urllib2
import urllib
from bs4 import BeautifulSoup
import urlparse
from scrapy.http import Request
from scrapy.http import Response
import re

class Spider(scrapy.Spider):
    name = 'Spider'
    root = "https://gupiao.baidu.com"
    start_urls = [
        'https://gupiao.baidu.com/stock/sz300187.html'
    ]