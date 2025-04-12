import sqlite3

# 1 - Conectar ao BD

def conecta_bd():
    conexao = sqlite3.connect('titulo.db')
    return conexao

# 2 - Inserir dados
def insere_dados(nome, ano, nota):
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
            INSERT INTO filmes(nome, ano, nota)
            VALUES(?,?,?)
        """,
        (nome,ano,nota)
    )
    conexao.commit()
    conexao.close()


# 3 - listagem dos dados

def obter_dados():
    conexao = conecta_bd()
    cursor = conexao.cursor()
    cursor.execute(
        """
            SELECT * FROM filmes
        """
    )
    dados = cursor.fetchall()
    conexao.close()
    return dados