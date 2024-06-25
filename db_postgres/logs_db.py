from connection_db import connect_to_db


def create_log_table():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS activity_log (
            log_id SERIAL PRIMARY KEY,
            event_type VARCHAR(50),
            event_description JSON,
            event_date TIMESTAMP
            )
    """)
    print("Table 'activity_log' was created successfully ")

    conn.commit()
    conn.close()


create_log_table()
