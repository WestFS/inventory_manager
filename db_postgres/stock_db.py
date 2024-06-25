from connection_db import connect_to_db


def create_stock_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS stock (
                id SERIAL PRIMARY KEY,
                product_name VARCHAR(255),
                category_product VARCHAR(50),
                quantity_product INTEGER,
                unit_price NUMERIC(10, 2),
                total_price NUMERIC(10, 2),
                date_product TIMESTAMP
            )
        ''')
    print("Table 'stock' was created successfully ")

    conn.commit()
    conn.close()


create_stock_table()
