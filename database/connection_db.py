import psycopg2


# Função para conectar ao banco de dados
def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="SENHA DE BANCO"
    )
