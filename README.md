# Solução Data-Pirates-challenge

Solução para o desafio https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md

## Escopo do desafio

- URL: http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm;

- Extrair da dados de pelo menos dois estados. Quanto mais, melhor;

- Coletar todos os registros de cada estado;

- Cada registro deve conter **pelo menos** 3 campos: "localidade", "faixa de cep" and um "id" gerado. Não permita registros duplicados no arquivo de saída.

- The output format must be [JSONL](http://jsonlines.org/)

  

## Requisitos

- Python 3.8;

- Scrapy 2.4.1;



## Instalar

### Criar virtualenv

**Mac OS / Linux:**

```bash
pip install virtualenv
virtualenv -p python3.8 venv
source venv/bin/activate
```

**Windows:**

```bash
pip install virtualenv
virtualenv -p python3.8 venv
venv\Scripts\activate
```

### Git:

```bash
git clone --depth=1 https://github.com/GabrieldeFreire/Data-Pirates-challenge.git
cd Data-Pirates-challenge
pip install -r requirements.txt
```



## Utilização

**Exemplos:**

- `scrapy crawl faixa_cep` - Raspa todos os estados.

- `scrapy crawl faixa_cep -a states=SP,ES` - Raspa os estados São Paulo (SP) e Espírito Santo (ES).

**Estados:**
- Acre (AC)
- Alagoas (AL)
- Amapá (AP)
- Amazonas (AM)
- Bahia (BA)
- Ceará (CE)
- Distrito Federal (DF)
- Espírito Santo (ES)
- Goiás (GO)
- Maranhão (MA)
- Mato Grosso (MT)
- Mato Grosso do Sul (MS)
- Minas Gerais (MG)
- Pará (PA)
- Paraíba (PB)
- Paraná (PR)
- Pernambuco (PE)
- Piauí (PI)
- Rio de Janeiro (RJ)
- Rio Grande do Norte (RN)
- Rio Grande do Sul (RS)
- Rondônia (RO)
- Roraima (RR)
- Santa Catarina (SC)
- São Paulo (SP)
- Sergipe (SE)
- Tocantins (TO)


## Saída
- Arquivo output.jsonl