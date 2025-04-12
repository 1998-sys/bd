from conexao_post import conn

cursor_obj = conn.cursor()

cursor_obj.execute('SELECT * FROM GAMES')

result = cursor_obj.fetchall()

print(result)