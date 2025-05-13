from db import get_db_connection

# Function to create a table to store the model
def create_storage_table_pipeline():
    sql = get_db_connection()

    cursor = sql.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS model_store_pipeline (
        id INT AUTO_INCREMENT PRIMARY KEY,
        model_pipeline VARCHAR(100),
        model_blob LONGBLOB
    )
    """)

    sql.commit()
    cursor.close()
    sql.close()

# model_store_pipeline = TABLE
# model_blob = COLUMN containing the model
# model_pipeline = COLUMN also the name of the model