# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from stack_overflow.items import StackOverflowItem
import json
import os

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
                data={}
                if os.path.exists('output.json'):
                    data=read()
                if selector.find_all('div')[0].text.partition(' ')[0].replace('\n','') in data.keys():
                    data[selector.find_all('div')[0].text.partition(' ')[0].replace('\n','')]+=1
                else:
                    data[selector.find_all('div')[0].text.partition(' ')[0].replace('\n','')]=1
                load(data)
                for d in data.keys():
                    print d
                item['url'] = selector.find_all('div')[0].text
                # if 'python' in selector.find_all('div')[0].text:
                #     number_of_python_posts += 1
                # elif 'java' in selector.find_all('div')[0].text:
                #     number_of_java_posts += 1
                # elif 'sql' in selector.find_all('div')[0].text:
                #     number_of_sql_posts += 1
                # elif '.net' in selector.find_all('div')[0].text:
                #     number_of_dotnet_posts += 1
                # elif 'php' in selector.find_all('div')[0].text:
                #     number_of_php_posts += 1
                # elif 'android' in selector.find_all('div')[0].text:
                #     number_of_android_posts += 1
                # else:
                #     number_of_other_posts += 1
            # with open('output.txt', 'w') as f:
            #     f.write(str(number_of_python_posts)+'\n')
            #     f.write(str(number_of_java_posts)+'\n')
            #     f.write(str(number_of_sql_posts)+'\n')
            #     f.write(str(number_of_dotnet_posts)+'\n')
            #     f.write(str(number_of_php_posts)+'\n')
            #     f.write(str(number_of_android_posts)+'\n')
            #     f.write(str(number_of_other_posts)+'\n')
            yield item

def load(data):
    with open('output.json','w') as f:
        json.dump(data,f)

def read():
    data={}
    with open('output.json','r') as f:
        data=json.load(f)
    return data