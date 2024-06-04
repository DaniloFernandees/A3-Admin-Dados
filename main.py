import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.stats.diagnostic as smd

# Carregar os dados do arquivo CSV
data = pd.read_csv("/content/plan_analisededados.csv")

# Filtrar as colunas necessárias
data = data[['Country', 'Year', 'Status', 'Population', 'Life expectancy ', 'GDP', 'percentage expenditure']]

# Separar os dados para o período de 2000 a 2015
data = data[(data['Year'] >= 2000) & (data['Year'] <= 2015)]

# Arredondar os valores da coluna 'Life expectancy' para duas casas decimais
data['Life expectancy '] = data['Life expectancy '].round(2)

# Listar os dados do Brasil
brazil_data = data[data['Country'] == 'Brazil']

# Listar os dados dos países em desenvolvimento
developing_countries = ['Russian Federation', 'Angola', 'Costa Rica', 'China', 'India', 'Mexico', 'Argentina', 'Peru', 'Panama', 'Ghana']
developing_data = data[data['Country'].isin(developing_countries)]

# Listar os dados dos países desenvolvidos
developed_countries = ['Italy', 'Iceland', 'Belgium', 'Germany', 'Denmark', 'Ireland', 'Austria', 'Japan']
developed_data = data[data['Country'].isin(developed_countries)]

# Comparar a expectativa de vida do Brasil com os países em desenvolvimento e desenvolvidos
brazil_vs_developing = brazil_data.merge(developing_data, on='Year', suffixes=('_Brazil', '_Developing'))
brazil_vs_developed = brazil_data.merge(developed_data, on='Year', suffixes=('_Brazil', '_Developed'))

# Visualizar a comparação entre Brasil e países em desenvolvimento
plt.figure(figsize=(10, 6))
sns.lineplot(data=brazil_vs_developing, x='Year', y='Life expectancy _Brazil', label='Brazil')
sns.lineplot(data=brazil_vs_developing, x='Year', y='Life expectancy _Developing', label='Developing Countries')
plt.title('Comparação da Expectativa de Vida: Brasil vs. Países em Desenvolvimento')
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida')
plt.legend()
plt.show()

# Visualizar a comparação entre Brasil e países desenvolvidos
plt.figure(figsize=(10, 6))
sns.lineplot(data=brazil_vs_developed, x='Year', y='Life expectancy _Brazil', label='Brazil')
sns.lineplot(data=brazil_vs_developed, x='Year', y='Life expectancy _Developed', label='Developed Countries')
plt.title('Comparação da Expectativa de Vida: Brasil vs. Países Desenvolvidos')
plt.xlabel('Ano')
plt.ylabel('Expectativa de Vida')
plt.legend()
plt.show()

# Calcular a média ponderada da expectativa de vida dos países comparados
def weighted_average_life_expectancy(df):
    return np.average(df['Life expectancy _Brazil'], weights=df['Population_Brazil'])

weighted_average_developing = weighted_average_life_expectancy(brazil_vs_developing)
weighted_average_developed = weighted_average_life_expectancy(brazil_vs_developed)

print("Média Ponderada da Expectativa de Vida (Países em Desenvolvimento):", round(weighted_average_developing, 2))
print("Média Ponderada da Expectativa de Vida (Países Desenvolvidos):", round(weighted_average_developed, 2))

# Calcular a média do valor gasto com saúde (percentage expenditure)
mean_percentage_expenditure_developing = developing_data['percentage expenditure'].mean()
mean_percentage_expenditure_developed = developed_data['percentage expenditure'].mean()

print("Média do Valor Gasto com Saúde (Países em Desenvolvimento):", round(mean_percentage_expenditure_developing, 2))
print("Média do Valor Gasto com Saúde (Países Desenvolvidos):", round(mean_percentage_expenditure_developed, 2))

# Relatório - Melhor e pior desempenho no aumento da expectativa de vida
max_increase_country = brazil_vs_developing.loc[brazil_vs_developing['Life expectancy _Developing'].idxmax()]['Country_Developing']
min_increase_country = brazil_vs_developing.loc[brazil_vs_developing['Life expectancy _Developing'].idxmin()]['Country_Developing']

print("Melhor desempenho no aumento da expectativa de vida (Países em Desenvolvimento):", max_increase_country)
print("Pior desempenho no aumento da expectativa de vida (Países em Desenvolvimento):", min_increase_country)

# Análise exploratória
print("\nAnálise Exploratória (Países em Desenvolvimento):")
print(developing_data.describe())

# Análise estatística
print("\nAnálise Estatística (Países em Desenvolvimento):")
print(developing_data.dtypes)

# Exemplo de função para carregar dados e filtrar por ano (modifique conforme necessário)
def carregar_e_filtrar_dados(filepath, ano_inicio, ano_fim):
    try:
        data = pd.read_csv(filepath)
        data_filtered = data[(data['Year'] >= ano_inicio) & (data['Year'] <= ano_fim)]
        return data_filtered
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        return None
    except pd.errors.EmptyDataError:
        print("Arquivo está vazio.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
