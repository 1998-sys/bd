from conexao_post import conn


cursor = conn.cursor()

games = [
    ('The Las of us II', 2020, 9.5),
    ('Spider man 2', 2023, 10)
]

for game in games:
    cursor.execute(
        """
        INSERT INTO games (name, year, score)
        VALUES (%s, %s, %s)
    """, game
    )

conn.commit()
print('Dados inseridos com sucesso !')
conn.close()