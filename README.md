# PROJETO DE EXTENSAO

# **Projeto de Extensão**

Para a utilização do IMS, o aplicativo de Gerenciamento de Estoque, são necessários os seguintes passos:

**1. Instalação do PostgreSQL**

2. Ter o python instalado em sua maquina

3.  Tenha GIT em sua maquina e utilize o seguinte comando no GITBASH
        git clone [https://github.com/WestFS/inventory_manager.git](https://github.com/WestFS/inventory_manager.git)

Você tambem pode descompactar o arquivo .zip e abra-o em sua IDE de preferência.

[inventory_manager-main.zip](PROJETO%20DE%20EXTENSAO%2038fddba15ee44cb48bc1254d6a39eb61/inventory_manager-main.zip)

É necessário ter certas bibliotecas instaladas em sua IDE, sendo elas:

- `pip install Pillow`
- `pip install customtkinter`
- `pip install tkinter`
- `pip install psycopg2`

Além disso, é necessário alterar a senha do arquivo connection_db.py e colocar a sua do POSTGRESQL para conectar ao banco PostgreSQL com o aplicativo.

import psycopg2


# Função para conectar ao banco de dados
def connect_to_db():
    return psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="ALTERE SUA SENHA DE BANCO"
    )


Crie essas tabela no POSTGRESQL ou execute as pastas que tem dentro do aplicativo IMS, só assim voce utilizará  o IMS

Essa de users é necessario ser criada dentro do POSTGRESQL

CREATE TABLE users(
id SERIAL PRIMARY KEY,
username VARCHAR(50) NOT NULL,
password VARCHAR(50) NOT NULL,
CONSTRAINT user_username_key UNIQUE (username)
);

CREATE TABLE IF NOT EXISTS stock (
id SERIAL PRIMARY KEY,
product_name VARCHAR(255),
category_product VARCHAR(50),
quantity_product INTEGER,
unit_price NUMERIC(10, 2),
total_price NUMERIC(10, 2),
date_product TIMESTAMP
)

CREATE TABLE IF NOT EXISTS activity_log (
log_id SERIAL PRIMARY KEY,
event_type VARCHAR(50),
event_description JSON,
event_date TIMESTAMP
)
