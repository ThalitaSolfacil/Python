from lib2to3.pgen2.pgen import DFAState
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# 1. Importando o csv
df = pd.read_csv("https://raw.githubusercontent.com/gurezende/Studying/master/Datasets/Cars.csv")
    # utilizar somente algumas colunas: usecols = [lista de colunas] 
    # utilizar somente algumas linhas: nrows = quantidade de linhas
    # interpretação de valores nulos: na_values = valor_nulo
 
# 2. Mostrando o formato do DataFrame
type(df)  # Devolve o tipo da variável (DataFreme)
df.dtypes # Devolve o tipo de valor em cada coluna

df.shape # Devolve o tamanho do Dataframe (linhas, colunas)
df.columns # Devolve uma lista do nome das colunas
df.info # Devolve dtypes, shape e columns


# 3. Mostra regiões do dataframe
df.head() # Devolve as 5 primeiras linhas (podendo especificar) 
df.tail() # Devolve as 5 últimas linhas (podendo especificar)


# 4. Alterando a estrutura do dataframe
df.columns = ['fabricante', 'modelo', 'tipo_veiculo', 'preco', 'tem_motor', 'potencia_hp', 'entre_eixos', 'largura', 'comprimento','peso',  'cap_combustivel', 'eficiencia', 'ultima_versao', 'power_perfect_factor', 'milhagem']
df = df.astype({'comprimento':  'object', 'peso': 'object'})

df [0:3]  # Devolve as três primeiras linhas
df[['fabricante', 'preco']] # Devolve apenas algumas colunas
df.loc[10:12, ['fabricante', 'preco']] # Recorta o Dataframe de acordo com o nome do index
df.iloc[10:12, 0:3] # Recorta o Dataframe de acordo com o índice



# 5. Filtrando dados
condicao = df.preco > 20 # Seleciona as linhas, dentro da coluna preco, que são maiores que 20
df[condicao]

df.query('preco >= 40', engine = 'python')  # Seleciona as linhas, dentro da coluna preco, que são maiores que 40

df.isnull() # Verifica se tem algum dado nulo
# df.isnull().sum().to_Frame().T # Tranforma em um Dataframe os valores nulos, transpostando as linhas e colunas
df.fillna(0) # Preenche os valores Nas com algum valor
df = df.dropna() # Remove os valores nulos

df.mean() # Devolve a média de cada coluna
df.median() # Devolve a mediana de cada coluna
df.interpolate() # Devolve algum valor, de acordo com os valores anteriores

df.describe() # Descreve estatísticas dentro do Dataframe
df.describe(include = 'object') # Descreve estatísticas dentro do Dataframe, somente em colunas tipo object

df.drop([55], inplace = True, axis = 0) # Remove uma linha específica

df.groupby('fabricante')['preco'].mean().sort_values() # Agrupa o dataframe de acordo com o fabricante
    # df.groupby(<grupo>)[<coluna para calcular>].function
df.groupby('fabricante').agg({'preco': ['mean', 'min'], 'potencia_hp': 'mean', 'eficiencia': 'mean', 'milhagem': 'mean'}).sort_values(by= ('preco', 'mean')) 



''' Problema 1: Encontre um carro que custe menos que 25k, tenha comprimento menor que 190 e com maior eficiencia e potencia possiveis '''

carro = df[(df.preco < 25) & (df.comprimento < 190)]
carro = carro[['fabricante', 'modelo', 'preco', 'comprimento', 'eficiencia', 'potencia_hp']]
# print(carro.sort_values(by = ['eficiencia', 'potencia_hp'], ascending= False))




# Resolução do professor

plt.figure(figsize= (25,9))


ordem = df.groupby('fabricante').preco.mean().sort_values().index

g1 = sns.boxplot(data = df, x = 'fabricante', y = 'preco', order = ordem) # Cria um grático de barra
plt.xticks(rotation = 30) # Configura os nomes no eixo x (não fica grudado um ao outro)
plt.hlines(y = 25, xmin = 0, xmax = len(ordem), linestyles = '--', color = 'red') # Cria uma linha em 25k
# plt.show()




# Fazendo gráfico de distribuição no pandas
carro.plot(kind = 'scatter',  x = 'potencia_hp', y = 'preco', s = 'eficiencia', figsize = (14, 6))
# Fazendo no plotly
fig = px.scatter(carro, x = 'potencia_hp', y = 'preco', size = 'eficiencia', color = 'eficiencia', hover_data= ['fabricante', 'modelo'])
fig.show()