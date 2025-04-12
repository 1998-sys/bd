import sqlite3

# Conectando ao banco de dados

conexão = sqlite3.connect('titulo.db')
cursor = conexão.cursor()

# Leitura de Dados

dados = cursor.execute(
    """
        SELECT * FROM filmes
    """)

print(dados.fetchall())