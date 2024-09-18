import sqlite3

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

    def chegou_no_estoque(self, id_produto, quantidade_chegou):
        self.cursor.execute("SELECT quantidade FROM Estoque WHERE id = ?", (id_produto,))
        quantidade_atual = self.cursor.fetchone()

        if quantidade_atual:
            nova_quantidade = quantidade_atual[0] + quantidade_chegou
            self.atualizar_quantidade(id_produto, nova_quantidade)
            print(f"Nova quantidade do produto ID {id_produto}: {nova_quantidade}")
        else:
            print("Produto não encontrado no estoque.")
    
    def saiu_do_estoque(self, id_produto, quantidade_saiu):
        self.cursor.execute("SELECT quantidade FROM Estoque WHERE id = ?", (id_produto,))
        quantidade_atual = self.cursor.fetchone()

        if quantidade_atual:
            nova_quantidade = quantidade_atual[0] - quantidade_saiu
            self.atualizar_quantidade(id_produto, nova_quantidade)
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
            quantidade = int(input("Quantidade que chegou: "))
            gerenciador.chegou_no_estoque(id, quantidade)
        elif escolha == 7:
            id = int(input("Id do produto: "))
            quantidade = int(input("Quantidade saiu do estoque: "))
            gerenciador.saiu_do_estoque(id, quantidade)
        elif escolha == 8:
            nome = input("Digite o nome do produto: ")
            gerenciador.localizar(nome)
        escolha = int(input("Digite o número desejado ou 0 para sair: "))



menu_estoquista()
gerenciador.fechar()
