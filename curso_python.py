import csv
import requests as r

'''  Conceitos básicos   '''
# a divisão de dois inteiros resulta em um float
# a divisão inteira resulta em um int (//)




'''   Listas  '''
# a lista, em python, é naturalmente um ponteiro
lista = [1, 2, 3, 4]
lista[-1] # acessa o último elemento
lista [1:3] # = lista[1], lista [2]
lista [2:] # = lista[2] - ultimo item
lista [:2] # = lisa [0], lista[1]
lista [0: 5: 2] # pula de 2 em 2
1 in lista # verifica se o valor está na lista (true or false)

lista.append(5) # coloca um elemento novo ao final da lista.
lista.remove(5) #deleta um elemento da lista (mas dá erro se o elemento não existir).
lista.count(1) #conta quantas vezes um elemento aparece.
lista.index(3) #busca um elemento e fala em qual posição ele aparece.
lista.sort() #ordena uma lista.
#As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor.






'''  Tuplas  '''
# Na tupla, ao invés de colchetes, usamos parênteses para declarar as tuplas.
tupla = (1, 2)
tupla2 = 1, #tupla unica
# tuplas são imutáveis: não é possível adicionar ou modificar valores. Armazena menos valores
# tupla armazena menos valores
a, b = tupla # unpacking (coloca os valores em variavies)






'''   Strings '''
# strings são imutaveis, mas podem ser transformadas em listas 
frase = "oi"
nome = " Thalita"
frase + nome # oi, Thalita
nome * 2 #ThalitaThalita

# para ignorar aspas: string1 = "\"oi"\"
# join() intercala cada elementos de uma lista com uma string
# pode ser usada em string vazia para converter uma lista a uma string

nome = "Lucas"
string = '-'.join(frase)
#Saída: L-u-c-a-s

frase.capitalize() # 1a letra maiúscula, restante minúscula
frase.title() # todo início de palavra em maiúscula, resto minúscula
frase.upper() # string inteira em maiúscula
frase.lower() # string inteira em minúscula
frase.replace('F', 'C') # substitui a primeira substring pela segunda
frase.split(",") # quebra uma string sempre que visualizar o caractere
frase.strip() # exclui espaços excessivos
 

email = "Olá, {}! Como vai?".format("Thalita") # Inclui um valor na string
# Pode-se chamar as variávies em diferentes ordens:
# print('{2}, {1} and {0}'.format('a', 'b', 'c'))
# Saída: c, b and a

# Podemos especificar um número de dígitos obrigatório por campo.
dia = 1
mes = 8
ano = 2019
data2 = '{:2d}/{:2d}/{:4d}'.format(dia, mes, ano)
# A opção 'd' significa que o parâmetro é um número inteiro.
# print(data2)
# Saída:  1/ 8/2019

# Podemos forçar que os espaços em branco sejam preenchidos com o número 0:
data3 = '{:02d}/{:02d}/{:04d}'.format(dia, mes, ano)
# print(data3)
# Saída: 01/08/2019

# Um modo mais simples de utilizar o format
nome = "Pietro"
profissao = "professor"
escola = "Let's Code"

# print(f"{nome} é {profissao} da {escola}.")
# Saída: Pietro é professor da Let's Code.





'''   Dicionário   '''
# O dicionário é definido pelos símbolos { e }
dicionario = {}
# O dicionário não possui um "append", mas são mutáveis.

# Adicionamos valores diretamente:
dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}

# Podemos utilizar o operador "in" para verificar se uma chave existe:
'cat' in dicionario
    
chaves = dicionario.keys()
# print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
# print(valores)
# Saída:dict_values(['gato', 'cão', 'rato'])

# para poder atribuir dados de um dicionário, sem que altere o original
dados_originais = {"Nome": "Thalita", "Cidade":"São Paulo"}
dados_copiados = dados_originais.copy()

#para atualizar valores, basta utilizar a função update
novos_dados = {"Nome" : "Lucas", "Nascimento" : "26/08/1999"}
dados_originais.update(novos_dados)

# Já a função .items(), retorna uma lista de tuplas (chave, valor) de um dicionário
itens = dicionario.items()
# print(itens)
# Saída:dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])

# A função get retorna se um valor existe ou não no dicionário
dicionario.get("pássaro")
# return = None






'''    Funções    '''
# funcoes:
def hello(*args): #aceita qualquer tipo de argumento, armazena como tupla
   print("Olá, mundo!")


def piscina(prof, **infos): # o parâmetro infos é opcional, armazena como dicionario
    vol = prof*infos['largura']*infos['comprimento']
    return vol
volume = piscina(5, largura=4, comprimento=5)
# print('O volume é: ', volume)


# expandindo um dicionário
def piscina(prof, largura=4, comprimento=5):
    vol = prof*largura*comprimento
    return vol
infos = {'largura': 10, 'comprimento': 20}
volume = piscina(5, **infos)
# print('O volume é: ', volume)





'''    Manipulação de arquivos    '''

arquivo = open("domcasmurro.txt", "r", encoding = "utf-8") # não precisa colocar o diretório se está na mesma pasta
# modo de abertura: leitura (read) ou escrita (write)
texto = arquivo.read () #leitura do arquivo
linha = arquivo.readline() # lê uma linha específica
# for linha em arquivo  ---> já lê automaticamente uma linha
arquivo.close() # fecha a conexão com o arquivo


#não precisa abrir ou fechar o arquivo
with open ("domcasmurro.txt", "r", encoding = "utf-8") as arquivo1:
   arquivo1.read ()

with open ("criar_arquivo.txt", "w", encoding = "utf-8") as arquivo1: # cria um novo arquivo ou subescreve
    arquivo1.write("Oi!")

with open ("criar_arquivo.txt", "a", encoding = "utf-8") as arquivo1: # abre um arquivo existente para adicionar informações ao final
    arquivo1.write("Oi!")

# + permite alterar o arquivo existente (r+, w+, a+)






'''     Arquivo CSV    '''

# Com separeted vels = valores separados por virgula
# utiliza a biblioteca csv

with open("covid.csv", "r", encoding = "utf-8") as planilha:
    
    leitor = csv.reader(planilha)
    next(leitor) # ignora o cabeçalho
    for linha in leitor:
        a = linha
        # print(linha)

with open("teste.csv", "w", encoding= "utf-8", newline="") as arquivo_escrita: 
    #new line nao pula linha ao escrever dados
    escritor = csv.writer(arquivo_escrita)
    escritor.writerow(["Olá!"])
    escritor.writerow(["Como vai você?"])


# exemplo com dicionario
with open('email.csv', 'r') as emails:
    leitor = csv.DictReader(emails, delimiter=';') #a primeira linha é lida como um cabeçalho
    # for linha in leitor:
        # print(linha['Login email']) #podemos chamar um valor específico de cada linha pela chave no cabeçallho


with open('names.csv', 'w', newline='') as csvfile:
    chaves = ['first_name', 'last_name'] # definimos o cabeçalho
    writer = csv.DictWriter(csvfile, fieldnames=chaves) # especificamos o cabeçalho
    writer.writeheader() # escrevemos o cabeçalho
    writer.writerow({'first_name': 'Senhor', 'last_name': 'Batata'}) # escrevemos linhas com as chaves e valores
    writer.writerow({'first_name': 'Will', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Elon', 'last_name': 'Musk'})


# exemplo de sublistas
with open('tabelaExemplo.csv', 'w') as arquivo:
    escritor = csv.writer(arquivo, delimiter = ';', lineterminator = '\n') #criando um escritor
    lista = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    escritor.writerows(lista) # writerows escreve cada "sublista" da lista como uma linha

with open('tabelaExemplo.csv', "r") as arquivo:
    leitor = csv.reader(arquivo, delimiter = ';', lineterminator = '\n') #criando um leitor
    #print  ("O conteúdo do arquivo é:")
    # print(leitor)
    # for linha in leitor:
        # print(linha)
       



'''     Requests   '''

# requests é uma biblioteca que permite fazer requisições a uma API 
url = "https://api.exchangerate-api.com/v6/latest"
req = r.get(url)
dados = req.json()
reais = dados["rates"]["BRL"]
# print (req.status_code)
print (dados)