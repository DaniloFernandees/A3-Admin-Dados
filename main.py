#Imports, descrição das colunas e informações
import numpy as np
import pandas as pd
from tabulate import tabulate
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd
import matplotlib.ticker as ticker

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

print(df.info())

#Carregamento dos dados do arquivo XLSX
df = pd.read_csv('https://gist.githubusercontent.com/ograndlucius/1bd7811ad7276c12563f7d163e7d10e7/raw/b8b469c143366a2175dcdf92395d9d334997a998/who_db.csv')
display(df)

#Filtragem dos Dados para o Brasil
column = 'Country'
criteria = 'Brazil'

df_filtrado = df[df[column] == criteria]

print("Dados filtrados para o Brasil:")
print(tabulate(df_filtrado[['Year','Life expectancy ']], headers='keys', tablefmt='pipe', showindex=False))

if not df_filtrado.empty:
    plt.figure(figsize=(12, 6))
    plt.plot(df_filtrado['Year'], df_filtrado['Life expectancy '], marker='o', linestyle='-', color='skyblue')
    plt.xlabel('Ano')
    plt.ylabel('Expectativa de Vida (Anos)')
    plt.title('Expectativa de Vida no Brasil ao Longo dos Anos')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    plt.show()
else:
    print(f"A coluna '{column}' não foi encontrada nos dados ou não há dados para {criteria}.")


#Filtragem dos Dados comparando o Brasil com o Estados Unidos
df_filtrado = df[(df['Country'] == 'Brazil') | (df['Country'] == 'United States of America')]
df_brasil = df_filtrado[df_filtrado['Country'] == 'Brazil']
df_eua = df_filtrado[df_filtrado['Country'] == 'United States of America']

plt.figure(figsize=(10, 6))

plt.plot(df_brasil['Year'], df_brasil['Life expectancy '], marker='o', linestyle='-', color='b', label='Brasil')
plt.plot(df_eua['Year'], df_eua['Life expectancy '], marker='s', linestyle='-', color='r', label='Estados Unidos')

plt.title('Comparação da Expectativa de Vida: Brasil x EUA')
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida')

plt.legend()

plt.grid(axis='y', linestyle='--')

df_brasil_renamed = df_brasil.rename(columns={'Country': 'País', 'Life expectancy ': 'Expectativa de Vida'})
df_eua_renamed = df_eua.rename(columns={'Country': 'País', 'Life expectancy ': 'Expectativa de Vida'})

df_tabela = pd.concat([df_brasil_renamed, df_eua_renamed])

df_tabela = df_tabela.sort_values(by=['País', 'Year'])

print(tabulate(df_tabela, headers='keys', tablefmt='pipe', showindex=False))

plt.show

#Comparação entre Brasil e os países desenvolvidos

#Comparativo de Expectativa de Vida
developed_countries = [
    'Australia', 'Belgium', 'Brazil', 'Croatia', 'Germany',
    'Ireland', 'Italy', 'Japan', 'Portugal', 'Spain', 'United States of America'
]

df_developed = df[df['Country'].isin(developed_countries)]

plt.figure(figsize=(15, 10))

for country in developed_countries:
    country_data = df_developed[df_developed['Country'] == country]
    plt.plot(country_data['Year'], country_data['Life expectancy '], marker='o', label=country)

print("Tabela de Expectativa de Vida - Países Desenvolvidos")
print(tabulate(df_developed[['Country', 'Year', 'Life expectancy ']], headers='keys', tablefmt='grid'))

plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida')
plt.title('Comparação entre Brasil e os Países Desenvolvidos (Expectativa de Vida)')
plt.legend()
plt.grid(True)
plt.show()

#Comparativo de PIB
developed_countries = [
    'Australia', 'Belgium', 'Brazil', 'Croatia', 'Germany',
    'Ireland', 'Italy', 'Japan', 'Portugal', 'Spain', 'United States of America'
]

df_developed = df[df['Country'].isin(developed_countries)]

print("Tabela de PIB - Países Desenvolvidos")
print(tabulate(df_developed[['Country', 'Year', 'GDP']], headers='keys', tablefmt='grid'))

plt.figure(figsize=(15, 10))

for country in developed_countries:
    country_data = df_developed[df_developed['Country'] == country]
    plt.plot(country_data['Year'], country_data['GDP'], marker='o', label=country)

plt.xlabel('Ano')
plt.ylabel('PIB')
plt.title('Comparação do PIB entre Brasil e os Países Desenvolvidos')
plt.legend()
plt.grid(True)
plt.show()

#Comparativo de População
developed_countries = [
    'Australia', 'Belgium', 'Brazil', 'Croatia', 'Germany',
    'Ireland', 'Italy', 'Japan', 'Portugal', 'Spain', 'United States of America'
]

df_developed = df[df['Country'].isin(developed_countries)]

print("Tabela de População - Países Desenvolvidos")
print(tabulate(df_developed[['Country', 'Year', 'Population']], headers='keys', tablefmt='grid'))

plt.figure(figsize=(15, 10))

for country in developed_countries:
    country_data = df_developed[df_developed['Country'] == country]
    plt.plot(country_data['Year'], country_data['Population'], marker='o', label=country)

plt.xlabel('Ano')
plt.ylabel('População')
plt.title('Comparação da População entre Brasil e os Países Desenvolvidos')
plt.legend()
plt.grid(True)
plt.show()

#Comparação entre Brasil e os países em desenvolvimento

#Comparativo de Expectativa de Vida
undeveloped_countries = ['Angola', 'Chad', 'Ethiopia', 'Haiti', 'Malawi', 'Mali', 'Mozambique', 'Niger', 'Rwanda', 'Uganda']

df_undeveloped = df[df['Country'].isin(undeveloped_countries + ['Brazil'])]

plt.figure(figsize=(15, 10))

for country in undeveloped_countries + ['Brazil']:
    country_data = df_undeveloped[df_undeveloped['Country'] == country]
    plt.plot(country_data['Year'], country_data['Life expectancy '], marker='o', label=country)

print("Tabela de Expectativa de Vida - Países em Desenvolvimento")
print(tabulate(df_developed[['Country', 'Year', 'Life expectancy ']], headers='keys', tablefmt='grid'))

plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida')
plt.title('Comparação entre Brasil e os Países em Desenvolvimento (Expectativa de Vida)')
plt.legend()
plt.grid(True)
plt.show()

#Comparativo de PIB
undeveloped_countries = [
    'Angola', 'Chad', 'Ethiopia', 'Haiti', 'Malawi', 'Mali',
    'Mozambique', 'Niger', 'Rwanda', 'Uganda'
]

df_undeveloped = df[df['Country'].isin(undeveloped_countries + ['Brazil'])]

print("Tabela de PIB - Países Subdesenvolvidos")
print(tabulate(df_undeveloped[['Country', 'Year', 'GDP']], headers='keys', tablefmt='grid'))

plt.figure(figsize=(15, 10))

for country in undeveloped_countries + ['Brazil']:
    country_data = df_undeveloped[df_undeveloped['Country'] == country]
    plt.plot(country_data['Year'], country_data['GDP'], marker='o', label=country)

plt.xlabel('Ano')
plt.ylabel('PIB (em bilhões de USD)')
plt.title('Comparação do PIB entre Brasil e os Países Subdesenvolvidos')
plt.legend()
plt.grid(True)
plt.show()

#Comparativo de População
undeveloped_countries = [
    'Angola', 'Chad', 'Ethiopia', 'Haiti', 'Malawi', 'Mali',
    'Mozambique', 'Niger', 'Rwanda', 'Uganda'
]

df_undeveloped = df[df['Country'].isin(undeveloped_countries + ['Brazil'])]

print("Tabela de População - Países Subdesenvolvidos")
print(tabulate(df_undeveloped[['Country', 'Year', 'Population']], headers='keys', tablefmt='grid'))

plt.figure(figsize=(15, 10))

for country in undeveloped_countries + ['Brazil']:
    country_data = df_undeveloped[df_undeveloped['Country'] == country]
    plt.plot(country_data['Year'], country_data['Population'], marker='o', label=country)

plt.xlabel('Ano')
plt.ylabel('População')
plt.title('Comparação da População entre Brasil e os Países Subdesenvolvidos')
plt.legend()
plt.grid(True)
plt.show()
