from conexao_post import conn

cursor_obj = conn.cursor()


sql = """
    UPDATE games
    SET name = %s
    WHERE id = %s
"""

cursor_obj.execute(sql, ('FIFA 23', 3))
conn.commit()
print('Dados atualizados com sucesso !')
conn.close()