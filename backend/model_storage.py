from db import get_db_connection

def create_storage_table():
    sql = get_db_connection()

    cursor = sql.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS model_store (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        model_blob LONGBLOB
    )
    """)

    sql.commit()
    cursor.close()
    sql.close()