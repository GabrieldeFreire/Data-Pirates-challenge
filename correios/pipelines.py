# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.exceptions import DropItem  
import json  


class CorreiosPipeline:
    def process_item(self, item, spider):
        return item


class JsonWriterPipeline:

    def open_spider(self, spider):
        self.file = open('output.jl', 'w')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = json.dumps(ItemAdapter(item).asdict()) + "\n"
        self.file.write(line)
        return item

class DuplicatesPipeline(object):  
   def __init__(self): 
      self.ids = set() 

   def process_item(self, item, spider): 
      if item['id'] in self.ids: 
         raise DropItem("Duplicate item found: %s" % item) 
      else: 
         self.ids.add(item['id']) 
         return item