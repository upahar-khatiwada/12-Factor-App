from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
from import_model import get_model
import uvicorn
import os
from dotenv import load_dotenv
from logging_setup import setup_logger

logger = setup_logger(__name__)

load_dotenv()

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

if model is None:
    logger.error("Model is not loaded in api_creation.py")

@app.get("/")
async def read_root():
    return {"message": "House Price Estimator API is running!"}

@app.post("/predict")
async def root(input_data: Parameters):
    logger.info(f"Received input: {input_data}")

    df_input = pd.DataFrame([input_data.model_dump()])

    try:
        prediction_result = model.predict(df_input)
        prediction_value = float(prediction_result[0])
        logger.info(f"Predicted value: {prediction_value}")
        return {"result" : prediction_value}
    except Exception as e:
        logger.error(f"Error occured while predicting : {e}")
        return {"error": "Prediction failed"}


if __name__ == "__main__":
    # FOR LOGS
    logger.info("Logger set up done at api_creation.py")

    # IMPORTING VALUES FROM .ENV
    host = os.getenv("HOST")
    port = int(os.getenv("PORT"))

    uvicorn.run("api_creation:app", host=host, port=port, reload=True)