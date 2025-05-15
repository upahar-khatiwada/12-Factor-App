# from db import get_db_connection
# import io
# import joblib
# from logging_setup import setup_logger

# logger = setup_logger(__name__)

# logger.info("Logger setup done at import_model.py")

# try:
#     sql = get_db_connection()
#     cursor = sql.cursor()

#     logger.info("Database connected at import_model.py")

#     # model_blob = COLUMN containing the model
#     # model_store_pipeline = TABLE for storing the model
#     # model_pipeline = COLUMN and also the name for the model

#     get_model_query = "SELECT model_blob FROM model_store_pipeline WHERE model_pipeline = %s"
#     cursor.execute(get_model_query, ("model_pipeline",))

#     logger.info("Query executed at import_model.py")

#     result = cursor.fetchone()
#     model_blob = result[0]

#     model_io = io.BytesIO(model_blob)
#     model = joblib.load(model_io)
    
#     logger.info("Model successfully imported at import_model.py")

# except Exception as e:
#     logger.error(f"Error occured at import_model.py: {e}")


# def get_model():
#     return model

# if __name__ == "__main__":
#     logger.info("Logger setup done at model_storage.py")

from db import get_db_connection
import io
import joblib
from logging_setup import setup_logger

logger = setup_logger(__name__)
logger.info("Logger setup done at import_model.py")

model = None  # Define at module level to avoid NameError

try:
    sql = get_db_connection()
    if sql is None:
        raise ConnectionError("Database connection failed. Got None from get_db_connection().")

    cursor = sql.cursor()
    logger.info("Database connected at import_model.py")

    get_model_query = "SELECT model_blob FROM model_store_pipeline WHERE model_pipeline = %s"
    cursor.execute(get_model_query, ("model_pipeline",))
    logger.info("Query executed at import_model.py")

    result = cursor.fetchone()
    if result is None:
        raise ValueError("No model found in database.")

    model_blob = result[0]
    model_io = io.BytesIO(model_blob)
    model = joblib.load(model_io)

    logger.info("Model successfully imported at import_model.py")

except Exception as e:
    logger.error(f"Error occurred at import_model.py: {e}")
    model = None  # Explicitly set to None if failure occurs

def get_model():
    return model

if __name__ == "__main__":
    logger.info("Logger setup done at model_storage.py")
