import sqlite3

# Conectando ao bando de dados
conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

# 2 - Deletando dados na tabela
id = (1,2)

cursor.execute(
    """
    DELETE FROM filmes
    WHERE id in (?,?)
    """,
    id
)

conexao.commit()

print('Dados excluídos com sucesso !')
conexao.close()