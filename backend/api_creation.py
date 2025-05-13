from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from import_model import get_model

app = FastAPI()

class Parameters(BaseModel):
    CRIM : float
    ZN : float
    INDUS: float
    CHAS: int
    NOX: float
    RM: float
    AGE: float
    DIS: float
    RAD: int
    TAX: int
    PTRATIO: float
    B: float
    LSTAT: float

model = get_model()

@app.get("/")
async def read_root():
    return {"message": "House Price Estimator API is running!"}

@app.post("/predict")
async def root(input_data: Parameters):
    df_input = pd.DataFrame([input_data.model_dump()])
    prediction_result = model.predict(df_input)
    return {"result" : float(prediction_result[0])}