from scrapy import cmdline
import os

os.system('matplotlib_script.py')
os.remove('output.json')
cmdline.execute("scrapy crawl hot_crawler".split())
