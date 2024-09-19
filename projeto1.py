import sqlite3
from datetime import datetime

class Produto:
    def __init__(self, id, nome, categoria, quantidade, preco, localizacao):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

class GerenciadorEstoque:
    def __init__(self, db_name='Estoque.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.criar_tabela()
        self.criar_tabela_historico()



    def criar_tabela(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Estoque (
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                quantidade INTEGER,
                preco REAL NOT NULL,
                localizacao TEXT NOT NULL
            );
        ''')

    def criar_tabela_historico(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS HistoricoEstoque (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                id_produto INTEGER,
                nome_produto TEXT,
                tipo_operacao TEXT,  -- 'entrada' ou 'saida'
                quantidade INTEGER,
                data_hora TEXT,
                FOREIGN KEY (id_produto) REFERENCES Estoque(id)
            );
        ''')
        self.conn.commit()

    def adicionar_produto(self, produto):
        novo_produto = (produto.id, produto.nome, produto.categoria, produto.quantidade, produto.preco, produto.localizacao)
        self.cursor.execute("INSERT INTO Estoque VALUES (?,?,?,?,?,?)", novo_produto)
        self.conn.commit()

    def atualizar_quantidade(self, id_produto, nova_quantidade):
        self.cursor.execute("UPDATE Estoque SET quantidade = ? WHERE id = ?", (nova_quantidade, id_produto))
        self.conn.commit()

    def atualizar_preco(self, id_produto, novo_preco):
        self.cursor.execute("UPDATE Estoque SET preco = ? WHERE id = ?", (novo_preco, id_produto))
        self.conn.commit()

    def consultar_estoque(self):
        self.cursor.execute("SELECT * FROM Estoque")
        return self.cursor.fetchall()

    def remover_produto(self, id_produto):
        self.cursor.execute("DELETE FROM Estoque WHERE id = ?", (id_produto,))
        self.conn.commit()

    def chegou_no_estoque(self, id_produto,nome_produto, quantidade_chegou):
        self.cursor.execute("SELECT quantidade FROM Estoque WHERE id = ?", (id_produto,))
        quantidade_atual = self.cursor.fetchone()

        if quantidade_atual:
            nova_quantidade = quantidade_atual[0] + quantidade_chegou
            self.atualizar_quantidade(id_produto, nova_quantidade)
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('INSERT INTO HistoricoEstoque (id_produto,nome_produto, tipo_operacao, quantidade, data_hora)VALUES (?,?,"entrada",?,?)',(id_produto,nome_produto,quantidade_chegou,data_hora))
            self.conn.commit()
            print(f"Nova quantidade do produto ID {id_produto}: {nova_quantidade}")
        else:
            print("Produto não encontrado no estoque.")
    
    def saiu_do_estoque(self, id_produto,nome_produto, quantidade_saiu):
        self.cursor.execute("SELECT quantidade FROM Estoque WHERE id = ?", (id_produto,))
        quantidade_atual = self.cursor.fetchone()

        if quantidade_atual:
            nova_quantidade = quantidade_atual[0] - quantidade_saiu
            self.atualizar_quantidade(id_produto, nova_quantidade)
            data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.cursor.execute('INSERT INTO HistoricoEstoque (id_produto,nome_produto,tipo_operacao, quantidade, data_hora)VALUES (?,?,"saida",?,?)',(id_produto,nome_produto,quantidade_saiu,data_hora))
            self.conn.commit()
            print(f"Nova quantidade do produto ID {id_produto}: {nova_quantidade}")
        else:
            print("Produto não encontrado no estoque.")

    def gerar_relatorio(self):
        self.cursor.execute("SELECT nome, quantidade FROM Estoque")
        produtos = self.cursor.fetchall()
        for nome, quantidade in produtos:
            if quantidade <= 10:
                print(f"{nome}: Estoque baixo (Quantidade: {quantidade})")
            elif 11 <= quantidade <= 50:
                print(f"{nome}: Estoque ótimo (Quantidade: {quantidade})")
            else:
                print(f"{nome}: Excesso de estoque (Quantidade: {quantidade})")
    
    
    def localizar(self, nome):
        self.cursor.execute("SELECT localizacao FROM Estoque WHERE nome = ?", (nome,))
        resultado = self.cursor.fetchone()
        if resultado:
            localizacao = resultado[0]
            print(f"O produto {nome} está localizado no {localizacao}.")
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    
    
    def consultar_historico(self):
        self.cursor.execute('SELECT * FROM HistoricoEstoque')
        historico = self.cursor.fetchall()

        for registro in historico:
            print(registro)


    def remover_produto_historico_estoque(self):
        self.cursor.execute("DELETE FROM HistoricoEstoque")
        self.conn.commit()


    def fechar(self):
        self.conn.close()

# Exemplo de uso:
gerenciador = GerenciadorEstoque()

def menu_estoquista():
    print("""
        1- Para mostrar o estoque
        2- Para adicionar um produto ao estoque
        3- Para atualizar um produto
        4- Para remover um produto
        5- Para ver o relatório
        6- Para adicionar quantidade ao estoque
        7- Para remover quantidade do estoque
        8- Para locazaliar o produto
        9- Para ver o historico de movimentação
        10- Para remover todos os itens do HistoricoEstoque
        0- Sair
    """)
    escolha = int(input("Digite o número desejado: "))

    while escolha != 0:
        if escolha == 1:
            estoque = gerenciador.consultar_estoque()
            for produto in estoque:
                print(produto)
        elif escolha == 2:
            id = int(input("Id: "))
            nome = input("Nome: ")
            categoria = input("Categoria: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            localizacao = input("Localização: ")
            produto = Produto(id, nome, categoria, quantidade, preco, localizacao)
            gerenciador.adicionar_produto(produto)
        elif escolha == 3:
            id = int(input("Id do produto a ser atualizado: "))
            preco = float(input("Novo preço: "))
            gerenciador.atualizar_preco(id, preco)
        elif escolha == 4:
            id = int(input("Id do produto a ser removido: "))
            gerenciador.remover_produto(id)
        elif escolha == 5:
            gerenciador.gerar_relatorio()
        elif escolha == 6:
            id = int(input("Id do produto: "))
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade que chegou: "))
            gerenciador.chegou_no_estoque(id,nome, quantidade)
        elif escolha == 7:
            id = int(input("Id do produto: "))
            nome = input("Nome do produto: ")
            quantidade = int(input("Quantidade saiu do estoque: "))
            gerenciador.saiu_do_estoque(id,nome, quantidade)
        elif escolha == 8:
            nome = input("Digite o nome do produto: ")
            gerenciador.localizar(nome)
        elif escolha == 9:
            gerenciador.consultar_historico()
        elif escolha == 10:
            gerenciador.remover_produto_historico_estoque()
        escolha = int(input("Digite o número desejado ou 0 para sair: "))



menu_estoquista()
gerenciador.fechar()
