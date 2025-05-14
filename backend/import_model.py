from db import get_db_connection
import io
import joblib

sql = get_db_connection()
cursor = sql.cursor()

# model_blob = COLUMN containing the model
# model_store_pipeline = TABLE for storing the model
# model_pipeline = COLUMN and also the name for the model

get_model_query = "SELECT model_blob FROM model_store_pipeline WHERE model_pipeline = %s"
cursor.execute(get_model_query, ("model_pipeline",))

result = cursor.fetchone()
model_blob = result[0]

model_io = io.BytesIO(model_blob)
model = joblib.load(model_io)

def get_model():
    return model