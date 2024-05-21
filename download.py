import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

# URL base do site
url_base = "http://sefaz.ac.gov.br/2021/?p=11082"


def coletar_dados():
    response = requests.get(url_base)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')

    # Encontre os links das abas (isso pode variar dependendo da estrutura do HTML)
    divs = soup.find_all('div', {"data-tab": True})

    tables = []
    for div in divs:
        tables.extend(div.find_all('table'))

    all_data = []
    for table in tables:
        headers = [header.get_text(strip=True) for header in table.find_all('tr')[0]]
        rows = table.find_all('tr')

        for row in rows[1:]:  # Ignorar a primeira linha de cabeçalhos
            cells = row.find_all('td')
            data = [cell.get_text(strip=True) for cell in cells]
            all_data.append(data)

    df = pd.DataFrame(all_data, columns=headers)
    df.to_csv('dados_sefaz_ac.csv', index=False)
    print("Dados salvos em dados_sefaz_ac.csv")
