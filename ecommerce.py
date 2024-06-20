import mysql.connector# Importa a função mysql.connector para conectar ao banco de dados MySQL

class Usuario:# Define a classe Usuario
    def __init__(self, nome, telefone):#O método __init__ inicializa os atributos da classe Usuario  (Nome,telefone)
        self.nome = nome#  atributo nome da instância atribui o valor do parametro nome 
        self.telefone = telefone# o atributo telefone da instância atribui o valor do parametro telefone

class Produto:# cria a classe produtos
    def __init__(self, nome, preco, descricao, estoque):#O método __init__ inicializa os atributos da classe Usuario  (Nome,preço,descriçao e estoque)
        self.nome = nome#Atributo nome da instancia atribui o valor do parametro nome
        self.preco = preco#Atributo preco da instancia atribui o valor do parametro preco
        self.descricao = descricao#Atributo descriçao da instancia atribui o valor do parametro descriçao
        self.estoque = estoque#Atributo estoque  da instancia atribui o valor do parametro estoque

class SistemaDeecommerce:# cria uma classe sistemadeecommerce
    def __init__(self):# O método __init__ inicializa a conexão com o banco de dados
        self.conexao = mysql.connector.connect(# conecta ao banco de dados mysql
            host="localhost",#endereco do servidor do banco de dados
            user="root",# Nome do usuário do banco de dados
            password="he182555@",# senha do usuario
            database="ecommerce_db"# nome do banco de dados
        )
        self.cursor = self.conexao.cursor()# exercuta os comandos sql

    def adicionar_usuario(self):#definir o metodo adicionar usuario
        nome = input("Digite o nome do usuário: ")#solicita o nome do usuario 
        telefone = input("Digite o telefone do usuário: ")# solicita o telefone do usuario 
        usuario = Usuario(nome, telefone)#cria uma estancia da classe usuario
        sql = "INSERT INTO usuario (nome, telefone) VALUES (%s, %s)"#inserir na tabela usuario nome e telefone
        valores=(usuario.nome,usuario.telefone)# Define os valores a serem inseridos
        self.cursor.execute(sql, valores)#executar as variaveis sql e valores
        self.conexao.commit()# atualizar 
        print('Usuário adicionado com sucesso.')#Imprime mensagem de sucesso

    def adicionar_produto(self):#definir o metodo adicionar produto
        nome = input("Digite o nome do produto: ")# solicita o nome do produto
        preco = float(input("Digite o preço do produto: "))#solicita o preço do produto
        descricao = input("Digite a descrição do produto: ")# exibe a descriçao do produto 
        estoque = int(input("Digite a quantidade em estoque do produto: "))# exibe a quantidade do produto
        produto = Produto(nome, preco, descricao, estoque)#cria uma estancia da classe produto
        sql = "INSERT INTO produtos (nome, preco, descricao, estoque) VALUES (%s, %s, %s, %s)"#inserir na tabela produtos (nome,preço,descriçao,estoque)
        valores = (produto.nome, produto.preco, produto.descricao, produto.estoque)#definir os valores a serem inseridos 
        self.cursor.execute(sql, valores)# excutar a variavel ( sql,valores)
        self.conexao.commit()# atualizar ou confirmar  a transaçao
        print('Produto adicionado com sucesso.')#apos ser atualizado e validado mostrar na tela produto adicionado com sucesso

    def listar_usuarios(self):#definir o metodo listar o usuario
        self.cursor.execute("SELECT nome, telefone FROM usuario")#Executa o comando SQL para selecionar dados nome e telefone da tabela usuario
        usuarios  = self.cursor.fetchall()# recuperar os registro da transaçao
        for usuario in usuarios:# para cada usuario em usuarios imprimir o resultado da f string abaixo
            print(f"Nome: {usuario[0]}, Telefone: {usuario[1]}")# imprimir na tela 

    def listar_produtos(self):#definir o metodo listar o usuario
        self.cursor.execute("SELECT nome, preco, descricao, estoque FROM produtos")#Executa o comando SQL para selecionar dados nome,preço,descriçao,estoque  da tabela produtos
        produtos = self.cursor.fetchall()#recupera todos os registros selecionados
        for produto in produtos:#para cada produtos em produtos imprimir  o resultado
            print(f"Nome: {produto[0]}, Preço: {produto[1]}, Descrição: {produto[2]}, Estoque: {produto[3]}")# imprimir na tela 

    def fechar_conexao(self):# fecha a conexao
        self.cursor.close()# Fecha o cursor
        self.conexao.close()# Fecha a conexão com o banco de dados


    def menu(self): # Define o método menu
        while True:# Loop infinito para exibir o menu até que o usuário escolha sair
            print("Menu:")# imprimi o menu
            print("1. Adicionar usuário")# Opção 1 do menu
            print("2. Adicionar produto")# Opção 2 do menu
            print("3. Listar usuários")# Opção 3 do menu
            print("4. Listar produtos")# Opção 4 do menu
            print("5. Sair")# Opção 5 do menu
            escolha = input("Escolha uma opção: ")# Solicita que o usuário escolha uma opção

            if escolha == '1':# Se a escolha for 1
                self.adicionar_usuario()#Chama o método adicionar_usuario
            elif escolha == '2':#Se a escolha for 2
                self.adicionar_produto()#Chama o método adicionar_produto
            elif escolha == '3':#Se a escolha for 3
                self.listar_usuarios()#Chama o método listar_usuarios
            elif escolha == '4':#Se a escolha for 4
                self.listar_produtos()#Chama o método listar_produtos
            elif escolha == '5':#Se a escolha for 5
                self.fechar_conexao()#chama o metodo fechar conexao
                print("Conexão fechada. Saindo...")# Imprime mensagem de saída
                break#Encerra o loop e sai do menu
            else:# Se a escolha não for válida
                print("Opção inválida. Tente novamente.")#imprimir a mensagem de erro

# Instancia o sistema de e-commerce e exibe o menu
sistema = SistemaDeecommerce() # Cria uma instância da classe SistemaDeecommerce
sistema.menu() # Chama o método menu para exibir o menu e permitir a interação do usuário.