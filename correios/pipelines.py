# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem  
import os  


class CorreiosPipeline:
    def process_item(self, item, spider):
        return item


class DeleteJsonLinePipeline:

    def open_spider(self, spider):
        try:
            os.remove("output.jsonl")
        except OSError as e:
            pass


class DuplicatesPipeline(object):  
   def __init__(self): 
      self.ids = set() 

   def process_item(self, item, spider):
       if item['id'] in self.ids: 
           raise DropItem("Duplicate item found: %s" % item)
       self.ids.add(item['id'])
       return item