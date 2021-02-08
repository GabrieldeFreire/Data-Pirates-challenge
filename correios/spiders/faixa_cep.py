import scrapy
import unicodedata
import hashlib
from itertools import zip_longest
from six import string_types

class FaixaCepSpider(scrapy.Spider):
    name = 'faixa_cep'
    start_urls = ['http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm']

    def parse(self, response):
        ufs_xpath = response.xpath('//select[@class="f1col"]//@value')
        ufs = ufs_xpath.getall()
        ufs = list(filter(None, ufs))
        ufs = ['SP']
        # for uf in ufs:
        #     formdata = {'UF': uf}
        #     yield scrapy.FormRequest.from_response(response,formdata=formdata
        #     callback=self.parse2)
# from scrapy import FormRequest
# fetch(FormRequest('http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm', formdata={'UF': 'SP','qtdrow': '100','pagini': '1','pagfim': '100'}))

        formdata = {'UF': 'SP',
                    'qtdrow': '100',
                    'pagini': '1',
                    'pagfim': '100'
                    }
        yield scrapy.FormRequest.from_response(response, formdata=formdata,
                                               cb_kwargs={'uf':formdata['UF']},
                                               callback=self.pages_number)
    def pages_number(self, response, uf):
        pages_xpath = response.xpath('//div[@class="ctrlcontent"]/text()').getall()
        pages_text = [item.strip() for item in pages_xpath if 'de' in item][0]
        pages = int(pages_text.split()[-1])//100

        formdata = {'UF': 'SP',
                    'qtdrow': '100',
                    'pagini': '1',
                    'pagfim': '100'
            }
        number_scaping_columns = 4

        list_info = response.xpath('//table[@class="tmptabela"][last()]//tr//td//text()').getall()
        list_info  = [self.normalize(item.strip()) for item in list_info if isinstance(item, str)]
        list_info = [iter(list_info)] * number_scaping_columns
        list_info = zip_longest(*list_info, fillvalue='')

        for fields in list_info:
            localidade, faixa_de_cep, situacao, tipo_de_faixa = fields
            id_ = hashlib.md5(''.join(fields).encode('utf-8'))
            id_ = id_.hexdigest()

            yield{'id':id_,
                  'uf':uf,
                  'localidade':localidade,
                  'faixa_de_cep': faixa_de_cep,
                  'situacao':situacao,
                  'tipo_de_faixa':tipo_de_faixa
            }



        # yield scrapy.FormRequest.from_response(response, formdata=formdata, cb_kwargs={'uf':formdata['UF']},
        #                                        callback=self.pages_info)

        # def pages_info(self, response, uf):
        #     list_info = response.xpath('//table[@class="tmptabela"][last()]//tr//td//text()').getall()

        #     for index in range(0, len(list_info), 4):
        #         yield{'uf':uf,
        #               'localidade':list_info[index],
        #               'faixa_de_cep':list_info[index+1],
        #               'situacao':list_info[index+2],
        #               'tipo_de_Faixa':list_info[index+3]
        #         }
    def normalize(self, string):
        return unicodedata.normalize('NFD', string).encode('ascii', 'ignore').decode("utf-8")

    # def grouper(iterable, n, fillvalue=None):
    #     args = [iter(iterable)] * n
    #     return zip_longest(*args, fillvalue=fillvalue)