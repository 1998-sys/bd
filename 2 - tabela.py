import sqlite3

# 1 - Conectando ao banco de dados
conexao = sqlite3.connect('titulo.db')

# 2 - Criando o cursor (permiteme realizar operações no banco de dados)
cursor = conexao.cursor()

# 3 - Criando a tabela
cursor.execute(
    """
    CREATE TABLE filmes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota REAL NOT NULL

    );

    """
)

# 4 - Fechar conexão
conexao.close()
print('Tabela Criada com sucesso !')