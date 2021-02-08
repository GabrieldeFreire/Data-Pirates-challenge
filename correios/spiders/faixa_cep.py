import scrapy
import unicodedata
from itertools import zip_longest
from correios.items import FaixaCepLoader, FaixaCepItem

class FaixaCepSpider(scrapy.Spider):

    name = 'faixa_cep'
    start_urls = ['http://www.buscacep.correios.com.br/sistemas/buscacep/resultadoBuscaFaixaCEP.cfm']

    def parse(self, response):
        '''Gets all states from correios site and iterate through it'''

        ufs_xpath = response.xpath('//select[@class="f1col"]//@value')
        ufs = ufs_xpath.getall()
        ufs = filter(None, ufs)

        for uf in ufs:
            formdata={'UF': uf}
            yield scrapy.FormRequest.from_response(response,formdata=formdata, cb_kwargs={'uf':uf},
                                                   callback=self.pages_walk)

    def pages_walk(self, response, uf):
        '''Gets all pages states and iterate through it. If gets one page yield row info'''

        pages_xpath = response.xpath('//div[@class="ctrlcontent"]/text()').getall()
        pages_text = [item.strip() for item in pages_xpath if 'de' in item][0]
        pages = (int(pages_text.split()[-1])//100)+1

        if pages == 1:
            list_info = response.xpath('//table[@class="tmptabela"][last()]//tr//td//text()').getall()
            list_info  = [item.strip() for item in list_info if isinstance(item, str)]
            list_info = [iter(list_info)] * 4
            list_info = zip_longest(*list_info, fillvalue='')

            for fields in list_info:
                row = FaixaCepLoader(FaixaCepItem())
                fields_ = [uf] + list(fields)
                row.add_fields(fields_)
                yield row.load_item()
        else:
            for page in range(pages):
                pagini = str(((page)*100)+1)
                pagfim = str((page+1)*100)
                formdata = {'UF': uf,
                            'qtdrow': '100',
                            'pagini': pagini,
                            'pagfim': pagfim
                            }
                yield scrapy.FormRequest.from_response(response, formdata=formdata, cb_kwargs={'uf':uf},
                                                       callback=self.extract_info)

    def extract_info(self, response, uf):
        '''Yield row info'''
        
        list_info = response.xpath('//table[@class="tmptabela"][last()]//tr//td//text()').getall()
        list_info  = [item.strip() for item in list_info if isinstance(item, str)]
        list_info = [iter(list_info)] * 4
        list_info = zip_longest(*list_info, fillvalue='')

        for fields in list_info:
            row = FaixaCepLoader(FaixaCepItem())
            fields_ = [uf] + list(fields)
            row.add_fields(fields_)
            yield row.load_item()
