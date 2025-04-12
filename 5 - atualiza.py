import sqlite3

conexao = sqlite3.connect('titulo.db')
cursor = conexao.cursor()

#2 - Atualizando dados na tabela
id = 1 
cursor.execute(
    """
        UPDATE filmes SET nome = ?
        WHERE id = ?
    """,
    ("Homen Aranha", id)
)

conexao.commit()
print('Dados atualizados com sucesso !')
conexao.close()