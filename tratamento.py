import pandas as pd
import re
from unidecode import unidecode


def remove_special_characters(text):
    return re.sub(r'[^A-Za-z0-9\s]', '', text)

def remove_space(text):
    return text.replace(' ', '')


def tratar_dados():
    df = pd.read_csv('dados_sefaz_ac.csv')

    # Substituir pontos por nada (remover pontos de milhar) e vírgulas por pontos (separador decimal)
    df['FUNDEB'] = df['FUNDEB'].str.replace('.', '').str.replace(',', '.').astype(float)
    df['ICMS'] = df['ICMS'].str.replace('.', '').str.replace(',', '.').astype(float)
    df['IPVA'] = df['IPVA'].str.replace('.', '').str.replace(',', '.').astype(float)
    df['MUNICÍPIO'] = df['MUNICÍPIO'].apply(unidecode).apply(remove_space)

    # Agrupar por município e somar os valores
    df_grouped = df.groupby('MUNICÍPIO').sum().reset_index()
    df_grouped = df_grouped.round(2)
    # Salva os dados em um csv
    df_grouped.to_excel('dados_sefaz_ac_soma.xlsx', index=False)
