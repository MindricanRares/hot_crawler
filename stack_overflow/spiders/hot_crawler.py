# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from stack_overflow.items import StackOverflowItem
import json
import os
import urllib2
import urllib

class HotCrawlerSpider(scrapy.Spider):
    name = "hot_crawler"
    allowed_domains = ["http://stackoverflow.com/?tab=hot"]
    start_urls = (
        'http://stackoverflow.com/?tab=hot/',
    )

    def parse(self, response):

        soup = BeautifulSoup(response.body, 'lxml')
        selector_list = soup.find_all('div', {'class': 'summary'})
        for selector in selector_list:
            item = StackOverflowItem()
            if len(selector.find_all('div')) > 0:
                data = {}
                if os.path.exists('output.json'):
                    data = read()
                if selector.find_all('div')[0].text.partition(' ')[0].replace('\n', '') in data.keys():
                    data[selector.find_all('div')[0].text.partition(' ')[0].replace('\n', '')] += 1
                else:
                    data[selector.find_all('div')[0].text.partition(' ')[0].replace('\n', '')] = 1
                load(data)
            item['tag'] = selector.find_all('div')[0].text.partition(' ')[0].replace('\n', '')
            item['url'] = (selector.find_all('a', 'question-hyperlink')[0].get('href'))
            item['title'] = selector.find_all('a', 'question-hyperlink')[0].getText()
            yield item


def load(data):
    with open('output.json', 'w') as f:
        json.dump(data, f)


def read():
    with open('output.json', 'r') as f:
        data = json.load(f)
    return data


# def tinyurl(url):
#     tiny = "http://tinyurl.com/api-create.php?url=%s" % (url)
#     page = urllib2.urlopen(tiny)
#     tiny = page.read()
#     page.close()
#
#     return tiny
#
# def isgd(url, keyword=None):
#     isgdurl = 'http://is.gd/create.php?format=simple&url=' + \
#         urllib.quote(url)
#
#     # Allow for an optional keyword, instead of getting a random
#     # string of characters:
#     if keyword:
#         isgdurl += '&shorturl=' + keyword
#
#     page = urllib2.urlopen(isgdurl)
#     shorturl = page.read()
#     page.close()

    # Now check to make sure it worked:
    isgdurl = 'http://is.gd/forward.php?format=simple&shorturl=' + shorturl
    page = urllib2.urlopen(isgdurl)
    longurl = page.read()
    page.close()

    return shorturl