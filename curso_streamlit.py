import pandas as pd
import streamlit as st

st.header('Meu Primeiro APP :heart:')
title = 'Título'
st.markdown(f'# {title} ')
    # Formatação de textos

''' 
## Subtítulo 
''' # é considerado markdown
st.sidebar.selectbox('Escolha a página', ['Home', 'Gráficos']) # Cria uma barra lateral

dados = pd.read_csv('financiamentos_pr.csv', sep = ';', low_memory= False, usecols= ['id', 'data_de_nascimento', 'area_atuacao', 'produto', 'preco_do_produto', 'classe_tipo', 'valor_da_parcela'])

dados['valor_da_parcela'] = dados['valor_da_parcela'].astype('string')
dados['valor_da_parcela'] = dados['valor_da_parcela'].apply(lambda x: float((x[3:].replace('.', '')).replace(',', '.')))

options = st.selectbox('Selecione uma variável', ['area_atuacao', 'produto']) # Multiselect com apenas uma opção
st.dataframe(dados.groupby(options)['valor_da_parcela'].mean().sort_values(ascending= False)) 
st.write('---')

st.subheader('Tipos de texto')
st.latex('\int_a^bf(x)d(x) = F(b) - F(a)') # Fórmulas matemáticas
st.code('''
        def Funcao(x)
            return x++
''') # Códigos

st.table(pd.DataFrame({'Linha': ['pf', 'pj', 'pr'] })) # Tabela (sem interatividade, printa todas as linhas)



st.write('---')
st.subheader('Tipos de Input')
st.button('Não clique aqui')
st.checkbox('Muito menos aqui')
st.radio('Já disse, não clica!', ['Pula'] * 5)


st.slider('Slide me') # Barra de rolamento
st.select_slider('Slide to select', [1, 2, 3]) # Barra de rolamento (não entendi a diferença)
st.text_input('Put your short text') # Pequeno input de texto
st.text_area('Put your text') # Grande input de texto
st.number_input('Put your number') # Input de número
st.date_input('Put your date') # Input de dia
st.time_input('Put your time') # Input de tempo
st.file_uploader('Give me your file') # Input de arquivo
st.color_picker('Wether your color') # Input de cor


st.write('---')

st.subheader('Gráficos e Imagens')
plot = dados['area_atuacao'].value_counts().plot(kind = 'barh') # Barra vertical = bar
st.pyplot(plot.figure)
st.image('https://insightlab.ufc.br/wp-content/uploads/2020/01/datascience-1.png', use_column_width= 'always') 


# 1. Estudo de Markdown
#   Títulos:r
#       - '#': h1
#       - '##': h2
#       - '###': h3

#   Parágrafo:
#       - Espaço ao fim da linha: Parágrafo
#       - Dois espaços ao fim da linha: Quebra de linha

#   Estilos:  
#       - negrito: **palavra** ou __palavra__
#       - italico: *palavra* ou _palava_
#       - riscado: ~~palavra~~
#       - linha: --- ou ***
#       - comando: `comando`
#       - código: ``` código ```
#       - respostas: > reply

#   Listas:
#       - numerada:
#           1. palavra
#              1. palavra
#           1. palavra
       
#       - demarcada:
#           * palavra
#               * palavra
#           * palavrapip install streamlit --upgrade
#           - palavra

#       - to do list:
#           -[] to do
#           -[x] to do
#           -[] to do

#    Links/Imagens:   
#       - link: [Título](<url>)
#       - Imagem: ![Título](<url>)

#     Tabela:
#       col1|col2|col3
#       ---|---|---
#       1|Gustavo|8,5