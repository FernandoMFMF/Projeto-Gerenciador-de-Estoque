"""import sqlite3

#1 - Conectar ao banco de dados (ou criar um novo)
#Usando a função connect do modulo sqlite3 para se conectar a um banco de dados SQLite
#chamando 'exemplo.db'. Se o banco de dados nao existir , ele será criado automaticamente

conn = sqlite3.connect('exemplo.db')

#criar um objeto cursor
# O cursor é usado para executar comandos SQL no banco de dados.
#Ele atua como uma especie de ponteiro que percorre os resultados de consultas

cursor = conn.cursor()

#3 Definir o comando SQL para criar a tabela
#define uma string create_table que contém um comando SQL para criar uma tabela chamada produtos.
#esta tabela terá quatro colunas : id(chave primaria), nome(texto), preço(numero real) e estoque (numero inteiro)

#O IF NOT EXISTS garante que a tabela só será criada se ainda nao existir

create_table = '''
CREATE TABLE IF NOT EXISTS Produtos(
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    estoque INTEGER
);
'''
#Usa o metodo execute do objeto cursor para executar o comando SQL definido anteriormente e criar a tabela no banco de dados
#4 Executar o comando SQL para criar a tabela 
cursor.execute(create_table)


#5 Confirmar as alterações (commit)
#Após a execução bem-sucedida do comando SQL, usa o método commit no objeto de conexão (conn) para confirmar
#as alterações no banco de dados 
#Isso garante que as alterações sejam efetivamente aplicadas.
conn.commit()


#6 Fechar a conexão com o banco de dados
#Finalmente, você usa o metodo close no objeto de conexão para encerrar a conexão com o banco de dados.
#é uma pratica recomendada fechar a conexão após a conclusão das operações, para liberar recursos e
#evitar possiveis problemas de concorrencia

conn.close()


import sqlite3

#conectando com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#Dados de um novo produto
novo_produto = ('Camiseta',29.99,50)
#comando sql para inserir o novo produto na tabela
inserir_produto = "INSERT INTO Produtos (nome, preco, estoque) VALUES (?, ?, ?)"
#Executando o comando para inserção
cursor.execute(inserir_produto, novo_produto)
#Confirmando alterações
conn.commit()
#fechando a conexão 
conn.close()

import sqlite3
#visualizar o produto
#conectando com o banco de dados
conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
#comando sql para selecionar todos os produtos
selecionar_produtos = "SELECT * FROM Produtos"
#executando
cursor.execute(selecionar_produtos)
#Obtendo todos os registros e exibindo-os
produtos = cursor.fetchall()
for produto in produtos:
    print(produto)
#fechando

#atualizar
#novo preco e id do produto a ser atualizado
novo_preco = 24.99
produto_id = 1 #suponhamos que queremos atualizar o produto com ID 1
#comando para atualizar
atualizar_preco = "UPDATE Produtos SET preco = ? WHERE id = ?"
#Executando o comando de atualização
cursor.execute(atualizar_preco, (novo_preco, produto_id))
#confirmando
conn.commit()
conn.close()

#Excluir produto
import sqlite3

conn = sqlite3.connect('exemplo.db')
cursor = conn.cursor()
produto_id = 1

excluir_produto = "DELETE FROM Produtos WHERE id = ?"
cursor.execute(excluir_produto, (produto_id,))
conn.commit()
conn.close()


Aula2 pandas

import pandas as pd

#Criando tabela

exemplo_1 = [10, 20, 30, 40, 50]

#Criando uma series a partir da lista

series_1 = pd.Series(data = exemplo_1)

print(exemplo_1)
print(series_1)


import pandas as pd

#criando dicionario com pares chave - valor

Exemplo_2 = {'A':100, 'B':200, 'C': 300, 'D':400, 'F':500}

#Criando uma Series a partir de dicionario

series_2 = pd.Series(data = Exemplo_2)

print(Exemplo_2)
print(series_2)


import pandas as pd

url = 'https://www.fdic.gov/bank/individual/failed/banklist.html'

dfs = pd.read_html(url)


print(type(dfs))
print(len(dfs))


df_bancos = dfs[0]

print(df_bancos.shape)

print(df_bancos.dtypes)

print(df_bancos.head)




import pandas as pd

#criar dicionario com nomes e idades

dados = {
    'Nome': ['Alice', 'Bob', 'Carol', 'David','Eve'],
    'Idade': [25, 30, 22, 35, 28]
}
#Criar uma séria a partir do dicionario

serie_idades = pd.Series(dados['Idade'], index=dados['Nome'])
#exibir a serie de idades

print('Serie de idades')
print(serie_idades)

#calcular a media das idades
media_idades =  serie_idades.mean()

print('\nMedia de Idades: ', media_idades)

Aula3



import pandas as pd

df_selic = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.11/dados?formato=json')

print(df_selic.info())
print(df_selic)


#verificar a duplicidade de linhas passo muito importante  utilizando a função drop_duplicates()
df_selic.drop_duplicates(keep='last',inplace=True)
#mantem o ultimo registro
#atraves do parametro inplace=true, faz com que a transformação seja salva do Data Frame
#no nosso caso  nao existe linhas duplicadas 

from datetime import date
from datetime import datetime as dt

data_estracao = date.today()
df_selic['data_estracao'] = data_estracao
df_selic['responsavel'] = "Fernando"

print(df_selic.info())
df_selic.head()

print(df_selic.loc[0])
print(df_selic.loc[[0,20,70]])

teste = df_selic['valor'] < 0.01

print(type(teste))
print(teste)




import pandas as pd

#Criando um data frame com 5 linhas de dados

data = {
    'nome': ['Produto A','Produto B','Produto C','Produto A','Produto E',],
    'quantidade de itens comprados': [3, 1, 4, 3, 2],
    'tipo de iten': ['Eletrônico', 'Vestuário', 'Alimento', 'Eletrônico', 'Alimento'],
    'receita total': [120, 80, 60, 120, 90]
}

df = pd.DataFrame(data)

print(df)
df.drop_duplicates(keep='last', inplace= True)

print(df)

df['preço de item'] = df['receita total'] / df['quantidade de itens comprados']

itens_acima_de_50 = df[df['preço de item'] > 50]

print("Itens acima de 50 reais: ", itens_acima_de_50)

import matplotlib.pyplot as plt
import random

dados1 = random.sample(range(100), k=20)
dados2 = random.sample(range(100), k=20)
print(dados1)

plt.plot(dados1,dados2)
plt.show()






import pandas as pd

dados = {
    'Produto': ['A','B','C'],
    'qtde_vendida': [33, 50, 45]
}

df = pd.DataFrame(dados)

df.plot(x='Produto', y='qtde_vendida', kind='bar')

df.plot(x='Produto', y='qtde_vendida', kind='pie')

df.plot(x='Produto', y='qtde_vendida', kind='line')


import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid') #Opçções  darkgrid, whitegrid, dark, white, ticks

df_tips = sns.load_dataset('tips')

print(df_tips)

fig, ax = plt.subplots(1, 3, figsize=(15,5))

sns.barplot(data=df_tips, x='sex',y='total_bill', ax=ax[0])
#media por sexo

sns.barplot(data=df_tips, x='sex',y='total_bill', ax=ax[1], estimator=sum)
#o motivo pelo barplot muitas vezes se bseia nos parametros adicionais e na flexibilidade que ele oferece
#vamos dar destaque ao parâmetro estimator que por padrao calcula media

sns.barplot(data=df_tips, x='sex',y='total_bill', ax=ax[2], estimator=len)

#A função "barplot()" do Seaborn apresenta uma variedade de opções estatísticas,
#permitindo que os cientistas de dados escolhan a métrica que melhor se ajusta aos seus objetivos..
#Por exemplo, você pode calcular a soma, a contagem ou até mesmo outras métricas personalizadas.
#Isso é particularmente útil quando você deseja exibir informações diferentes nas barras,
#como a quantidade (len) ou a soma (sum) dos valores, en vez da média.


import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style='whitegrid') #Opçções  darkgrid, whitegrid, dark, white, ticks

df = sns.load_dataset('tips')

plt.figure(figsize=(8,5))
sns.barplot(x='time', y='total_bill', data=df, estimator=sum,errorbar=None, palette='Set2')
plt.xlabel('Periodo(time)')
plt.ylabel('Total gastos')
plt.title('Total de gastos por periodo (Almoço ou Jantar)')
plt.show()


#media
plt.figure(figsize=(8,5))
sns.barplot(x='time', y='total_bill', data=df)
plt.xlabel('Periodo(time)')
plt.ylabel('Media de gastos')
plt.title('Media de gastos por periodo (Almoço ou Jantar)')
plt.show()

#media da gorjeta
plt.figure(figsize=(8,5))
sns.barplot(x='time', y='total_bill', data=df, palette="Set3")
plt.xlabel('Periodo(time)')
plt.ylabel('Media da gorjeta')
plt.title('Media da gorjeta por periodo (Almoço ou Jantar)')
plt.show()


import sqlite3
#1 conectar ou criar se n existir
conn = sqlite3.connect('funcionarios.db')

#2 criar tabela

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
        nome TEXT,
        cargo TEXT,
        salario REAL
    )

''')

#3 INSERIR NOVO FUNCIONARIO NA TABELA

'''novo_funcionario = (2,'Mig', 'Gerente', 10000.00)
cursor.execute("INSERT INTO funcionarios VALUES (?, ?, ?, ?)", novo_funcionario)
conn.commit()'''

#4 consultar e exibir funcionarios

'''cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print('Funcionarios cadastrados: ')
for funcionario in funcionarios:
    print(funcionario)'''

#5 Atualização

atualização = ('fer', 5500.00, 1)
cursor.execute('UPDATE funcionarios SET nome = ? , salario = ? WHERE id = ?', atualização)
conn.commit


cursor.execute("SELECT * FROM funcionarios")
funcionarios = cursor.fetchall()
print('Funcionarios cadastrados: ')
for funcionario in funcionarios:
    print(funcionario)

#6 Deletar funcionario

id_funcionario_para_deletar = 2

cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario_para_deletar,))
conn.commit()

"""