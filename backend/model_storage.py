from db import get_db_connection
from logging_setup import setup_logger

logger = setup_logger(__name__)

logger.info("Logger setup done at model_storage.py")

# Function to create a table to store the model
def create_storage_table_pipeline():
    try:
        sql = get_db_connection()
        logger.info("Database connected at model_storage.py")
        cursor = sql.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS model_store_pipeline (
            id INT AUTO_INCREMENT PRIMARY KEY,
            model_pipeline VARCHAR(100),
            model_blob LONGBLOB
        )
        """)

        logger.info("Query executed at model_storage.py")

        sql.commit()
        cursor.close()
        sql.close()

    except Exception as e:
        logger.error(f"Error occured while creating storage for model: {e}")

# model_store_pipeline = TABLE
# model_blob = COLUMN containing the model
# model_pipeline = COLUMN also the name of the model
