import requests
from dotenv import load_dotenv
import os
import mysql.connector as connection
from dotenv import load_dotenv

load_dotenv()

API_URL = os.getenv("API_URL")
PREDICT_ENDPOINT = "predict"

test_payload = {
  "CRIM": 10,
  "ZN": 20,
  "INDUS": 30,
  "CHAS": 1,
  "NOX": 0,
  "RM": 1,
  "AGE": 34,
  "DIS": 0,
  "RAD": 5,
  "TAX": 0,
  "PTRATIO": 0,
  "B": 0,
  "LSTAT": 0
}

# Test for GET Request
def test_getRequest():
    response = requests.get(API_URL)
    assert response.status_code == 200, f"GET request failed with status code {response.status_code}"
    print("GET request passed")

# Test for POST Request
def test_postRequest():
    response = requests.post(API_URL + PREDICT_ENDPOINT, json=test_payload)
    assert response.status_code == 200, f"POST request failed with status code {response.status_code}"

# Test for connecting to database
def test_database_connection():
    assert connection.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        use_pure=True
    )