# Projeto de Expectativa de Vida - OMS

# Projeto para UC de Adminsitração de dados - 2024

Este projeto analisa dados de expectativa de vida, PIB per capita e gastos com saúde para diversos países, com foco especial no Brasil (2000-2015). Ele também gera estatísticas descritivas e gráficos para visualização dos dados.

## Componentes da Equipe:

- Thalyson da Silva Siqueira 
- Caio Lucius Nascimento Sales 
- Jailton Dayvid Silva de Morais 
- Danilo de Macêdo Fernandes
- Alexandre Nascimento Caminha 
- Vinicius Magno Ferreira da Cruz 

## Requisitos

- **Python** (versão 3.6 ou superior)
- **pip** (gerenciador de pacotes do Python)

## Passos para Instalação

Siga as etapas abaixo para configurar o ambiente e instalar todas as dependências necessárias.

### 1. Instalar Python e pip

1. Baixe e instale a versão mais recente do [Python](https://www.python.org/downloads/).
2. Certifique-se de marcar a opção "Add Python to PATH" durante a instalação.
3. Verifique se o Python e o pip foram instalados corretamente executando os comandos abaixo no Prompt de Comando:

   ```sh
   python --version
   pip --version

### 2. Clonar o Repositório

1. Abra o Prompt de Comando e navegue até a pasta onde deseja clonar o repositório.
2. Execute o comando abaixo para clonar o repositório:

   ```bash
   git clone
   ```
3. Navegue até a pasta do projeto:

   ```bash
   cd life_expectancy_A3   
   ```
### 3.Executar a Aplicação

1. Execute o arquivo "setup.bat" para instalar todas as dependências dentro de um ambiente virtual e executar o script principal.

   ```bash
   setup.bat
   ```

## Tratamento de dados e tópicos analisados:

O script principal index.py realiza várias etapas para analisar os dados de expectativa de vida, PIB per capita e gastos com saúde para diversos países, com foco especial no Brasil (2000-2015). Aqui está uma explicação detalhada de cada etapa do código:

### 1. Configuração Inicial
   ```python
   import pandas as pd

   pd.set_option('display.max_rows', None)
   pd.set_option('display.max_columns', None)

   df = pd.read_csv('life_expectancy_db.csv')

   print(df.head().to_markdown(index=False, numalign="left", stralign="left"))

   print(df.info()) 
   ```
   - *Configuração de exibição do pandas:* Define a exibição máxima de linhas e colunas.
   - *Leitura do arquivo CSV:* Carrega o arquivo life_expectancy_db.csv em um DataFrame.
   - *Exibição das primeiras* linhas: Mostra as primeiras 5 linhas do DataFrame.
   - *Informações do DataFrame:* Exibe informações sobre as colunas e tipos de dados.

### 2. Remoção de Espaços em Branco dos Nomes das Colunas

```python
df.columns = df.columns.str.strip()
```
Esta linha remove espaços em branco no início e no final dos nomes das colunas do DataFrame df. Isso garante que os nomes das colunas sejam consistentes e evita problemas com espaços extras.

### 3. Filtragem dos Dados para o Brasil

```python
df_brazil = df[df['Country'] == 'Brazil']
```
Esta linha filtra o DataFrame df para incluir apenas as linhas onde a coluna Country é igual a 'Brazil'. O resultado é um novo DataFrame df_brazil contendo apenas dados do Brasil.

### 4. Cálculo de Estatísticas Descritivas

```python
desc_stats = df_brazil[['Life expectancy', 'GDP', 'percentage expenditure']].describe()
desc_stats = desc_stats.round(2)
```
Essas linhas calculam estatísticas descritivas (como média, desvio padrão, mínimo, máximo, etc.) para as colunas Life expectancy, GDP e percentage expenditure do DataFrame df_brazil. Os valores são arredondados para duas casas decimais para facilitar a leitura.

### 5. Impressão das Estatísticas Descritivas

```python
print("Estatísticas Descritivas para o Brasil (2000-2015):\n")
print(desc_stats.to_markdown(numalign="left", stralign="left"))
```
Essas linhas imprimem as estatísticas descritivas calculadas no console, formatadas em Markdown para melhor legibilidade.

### 6. Exportação das Estatísticas Descritivas para CSV

```python
desc_stats.to_csv('desc_stats_brazil.csv', index=True)
```
Esta linha exporta as estatísticas descritivas para um arquivo CSV chamado desc_stats_brazil.csv.

### 7. Criação de Gráfico de Linha

```python
   df_brazil_melted = df_brazil.melt('Year', ['Life expectancy', 'GDP', 'percentage expenditure'])
   plt.figure(figsize=(10, 6))
   for label, df_group in df_brazil_melted.groupby('variable'):
      plt.plot(df_group['Year'], df_group['value'], marker='o', label=label)
   plt.title('Brasil: Expectativa de Vida, PIB per capita e Gastos com Saúde (2000-2015)')
   plt.xlabel('Year')
   plt.ylabel('Valores')
   plt.xticks(rotation=45)
   plt.legend()
   plt.grid(True)
   plt.tight_layout()

   plt.savefig('line_plot_brazil_life_expectancy_gdp_health_expenditure.png')

   plt.show()
```
Este bloco de código cria um gráfico de linha mostrando a evolução da expectativa de vida, PIB per capita e gastos com saúde ao longo dos anos no Brasil. O gráfico é salvo como um arquivo PNG e exibido na tela.

### 8. Cálculo da Média por País

```python
country_means = df.groupby('Country')[['Life expectancy', 'GDP', 'percentage expenditure']].mean()
```
Esta linha calcula a média da expectativa de vida, PIB per capita e gastos com saúde para cada país no DataFrame original df.

### 9. Ordenação e Impressão dos Países com Maior e Menor Expectativa de Vida

```python
country_means_sorted = country_means.sort_values(by='Life expectancy', ascending=False)

print("\nTop 10 países por expectativa de vida média (2000-2015):\n")
print(country_means_sorted.head(10).round(2).to_markdown(numalign="left", stralign="left"))

print("\nÚltimos 10 países por expectativa de vida média (2000-2015):\n")
print(country_means_sorted.tail(10).round(2).to_markdown(numalign="left", stralign="left"))
```
Essas linhas ordenam os países pela expectativa de vida média em ordem decrescente e imprimem os 10 países com maior e menor expectativa de vida no console,

```python
country_means_sorted.head(10).round(2).to_csv('top_10_countries_life_expectancy.csv', index=True)
country_means_sorted.tail(10).round(2).to_csv('bottom_10_countries_life_expectancy.csv', index=True)
```

Estas linhas exportam os dados dos 10 países com maior e menor expectativa de vida para arquivos CSV chamados top_10_countries_life_expectancy.csv e bottom_10_countries_life_expectancy.csv, respectivamente.
