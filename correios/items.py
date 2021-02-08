# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst, MapCompose, Join

import hashlib

class FaixaCepLoader(ItemLoader):
    default_output_processor = TakeFirst()
    def add_fields(self, fields):
        uf, localidade, faixa_de_cep, situacao, tipo_de_faixa = fields
        id = hashlib.md5(''.join(fields[1:]).encode('utf-8'))
        id = id.hexdigest()
        self.add_value('id', id)
        self.add_value('uf', uf)
        self.add_value('localidade', localidade)
        self.add_value('faixa_de_cep', faixa_de_cep)
        self.add_value('situacao', situacao)
        self.add_value('tipo_de_faixa', tipo_de_faixa)


class FaixaCepItem(Item):
    id = Field()
    uf = Field()
    localidade = Field()
    faixa_de_cep = Field()
    situacao = Field()
    tipo_de_faixa = Field()

class CorreiosItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
