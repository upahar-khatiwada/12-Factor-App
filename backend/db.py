# db.py
import os
import pandas as pd
import mysql.connector as connection
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return connection.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        use_pure=True
    )

def fetch_dataframe(query: str) -> pd.DataFrame:
    try:
        mydb = get_db_connection()
        df = pd.read_sql(query, mydb)
        mydb.close()
        print("Query executed successfully")
        return df
    except Exception as e:
        print(f"There was an error: {e}")
        return pd.DataFrame()  # Return empty DataFrame on failure
