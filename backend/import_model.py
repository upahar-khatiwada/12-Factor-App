from db import get_db_connection
import io
import joblib
import numpy as np

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

# TESTING

# X_dummy = np.array([[
#     0.2,     # CRIM
#     12.5,    # ZN
#     7.5,     # INDUS
#     0,       # CHAS
#     0.45,    # NOX
#     6.3,     # RM
#     65.0,    # AGE
#     4.2,     # DIS
#     4,       # RAD
#     300,     # TAX
#     18.5,    # PTRATIO
#     396.9,   # B
#     9.0      # LSTAT
# ]])

# print(float(model.predict(X_dummy)[0]))

def get_model():
    return model