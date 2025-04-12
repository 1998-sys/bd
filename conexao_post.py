import psycopg2

conn = psycopg2.connect(
    database='db_games',
    user = 'postgres',
    password = '987456mM',
    host = 'localhost',
    port = '5432'
)