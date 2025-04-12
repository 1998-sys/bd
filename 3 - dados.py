import sqlite3

# 1 - Conectando ao BD
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()


# 2 - Inserindo dados na tabela
cursor.execute(
    """
        INSERT INTO FILMES(nome, ano, nota)
        VALUES('Sonic', 2020, 8.0)
    """
)

conexao.commit() #Salva as alterações no banco de dados
conexao.close() #Fecha a conexão com o banco de dados

print('Dados inseridos na tabela !')