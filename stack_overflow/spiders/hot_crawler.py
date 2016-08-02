# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from stack_overflow.items import StackOverflowItem


class HotCrawlerSpider(scrapy.Spider):
    name = "hot_crawler"
    allowed_domains = ["http://stackoverflow.com/?tab=hot"]
    start_urls = (
        'http://stackoverflow.com/?tab=hot/',
    )

    def parse(self, response):
        number_of_java_posts = 0
        number_of_python_posts = 0
        number_of_sql_posts = 0
        number_of_dotnet_posts = 0
        number_of_php_posts = 0
        number_of_android_posts = 0
        number_of_other_posts = 0

        soup = BeautifulSoup(response.body, 'lxml')
        selector_list = soup.find_all('div', {'class': 'summary'})
        for selector in selector_list:
            item = StackOverflowItem()
            if len(selector.find_all('div')) > 0:
                item['url'] = selector.find_all('div')[0].text
                if 'python' in selector.find_all('div')[0].text:
                    number_of_python_posts += 1
                elif 'java' in selector.find_all('div')[0].text:
                    number_of_java_posts += 1
                elif 'sql' in selector.find_all('div')[0].text:
                    number_of_sql_posts += 1
                elif '.net' in selector.find_all('div')[0].text:
                    number_of_dotnet_posts += 1
                elif 'php' in selector.find_all('div')[0].text:
                    number_of_php_posts += 1
                elif 'android' in selector.find_all('div')[0].text:
                    number_of_android_posts += 1
                else:
                    number_of_other_posts += 1
            with open('output.txt', 'w') as f:
                f.write(str(number_of_python_posts)+'\n')
                f.write(str(number_of_java_posts)+'\n')
                f.write(str(number_of_sql_posts)+'\n')
                f.write(str(number_of_dotnet_posts)+'\n')
                f.write(str(number_of_php_posts)+'\n')
                f.write(str(number_of_android_posts)+'\n')
                f.write(str(number_of_other_posts)+'\n')
            yield item
