from scrapy import cmdline
import os

os.system('matplotlib_script.py')
cmdline.execute("scrapy crawl hot_crawler".split())
