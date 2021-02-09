# Solução Data-Pirates-challenge
Solução para o desafio https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md

## Escopo do desafio

- URL: http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm;

- Extrair da dados de pelo menos dois estados. Quanto mais, melhor;

- Coletar todos os registros de cada estado;

- Cada registro deve conter **pelo menos** 3 campos: "localidade", "faixa de cep" and um "id" gerado. Não permita registros duplicados no arquivo de saída.

- The output format must be [JSONL](http://jsonlines.org/)

  

## Requisitos
- Python 3.8.5;

- Scrapy 2.4.1;



## Instalar

**Git:**
```bash
git clone --depth=1 https://github.com/GabrieldeFreire/Data-Pirates-challenge.git
cd Data-Pirates-challenge
pip install -r requirements.txt
```



## Utilização

**Exemplos:**

- `scrapy crawl faixa_cep` - Raspa todos os estados.

- `scrapy crawl faixa_cep -a states=SP,ES` - Raspa os estados São Paulo (SP) e Espírito Santo (ES).

  

## Saída
- Arquivo output.jsonl

