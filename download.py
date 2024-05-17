import requests
from bs4 import BeautifulSoup, Tag
import re


def download():
    # URL do site que contém a tabela
    url = 'http://sefaz.ac.gov.br/2021/?p=11082'

    # Envia uma solicitação GET para a URL
    response = requests.get(url)

    # Verifica se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Parseia o conteúdo HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        # Encontra todos os elementos com a classe elementor-tab-content
        abas = soup.find_all(class_='elementor-tab-content')

        # Itera sobre as abas
        for aba in abas:
            # Verifica se a aba contém a tabela que você está procurando
            if "texto_unico_na_aba" in aba.get_text():
                # Encontra a tabela dentro da aba
                tabela = aba.find('table')

                # Verifica se a tabela foi encontrada
                if tabela:
                    # Extrai os dados da tabela
                    for linha in tabela.find_all('tr'):
                        # Extrai o texto de cada célula da linha
                        dados = [celula.get_text(strip=True) for celula in linha.find_all(['td', 'th'])]
                        print(dados)
                    break  # Termina o loop após encontrar a tabela desejada
    else:
        print('Falha ao acessar o site:', response.status_code)

# def download():
#     # URL do site que contém a tabela
#     url = 'http://sefaz.ac.gov.br/2021/?p=11082'
#
#     # Envia uma solicitação GET para a URL
#     response = requests.get(url)
#
#     # Verifica se a solicitação foi bem-sucedida (código de status 200)
#     if response.status_code == 200:
#         # Parseia o conteúdo HTML
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Encontra a div com a classe específica
#         # div_element = soup.find('div', id=re.compile(r'elementor-tab-content-'))
#         div_element = soup.find('div', class_='elementor-tabs')
#         # Verifica se a div foi encontrada
#         if div_element:
#             div_content_127 = soup.find('div', id=re.compile(r'elementor-tab-content-'))
#             # print(div_content_127)
#             for div in div_element:
#                 tabela = div.find('table')
#                 if isinstance(tabela, Tag):
#                     # Itera sobre as linhas da tabela e extrai os dados
#                     for linha in tabela.find_all('tr'):
#                         # Itera sobre as células da linha e extrai o texto
#                         dados = [celula.get_text(strip=True) for celula in linha.find_all(['td', 'th'])]
#                         print(dados)
#     else:
#         print('Falha ao acessar o site:', response.status_code)

# def download():
#     # URL do site que contém a tabela
#     url = 'http://sefaz.ac.gov.br/2021/?p=11082'
#
#     # Envia uma solicitação GET para a URL
#     response = requests.get(url)
#
#     # Verifica se a solicitação foi bem-sucedida (código de status 200)
#     if response.status_code == 200:
#         # Parseia o conteúdo HTML
#         soup = BeautifulSoup(response.content, 'html.parser')
#
#         # Encontra a div com a classe específica
#         # div_element = soup.find('div', id=re.compile(r'elementor-tab-content-'))
#         div_element = soup.find('div', class_='elementor-tabs')
#         print(div_element)
#
#         # Verifica se a div foi encontrada
#         if div_element:
#             # Encontra a tabela dentro da div
#             tabela = div_element.find('table')
#
#             # Verifica se a tabela foi encontrada
#             if tabela:
#                 # Itera sobre as linhas da tabela e extrai os dados
#                 for linha in tabela.find_all('tr'):
#                     # Itera sobre as células da linha e extrai o texto
#                     dados = [celula.get_text(strip=True) for celula in linha.find_all(['td', 'th'])]
#                     print(dados)
#             else:
#                 print('Tabela não encontrada dentro da div.')
#         else:
#             print('Div não encontrada com a classe específica.')
#     else:
#         print('Falha ao acessar o site:', response.status_code)
