import os
import pandas as pd
import mysql.connector as connection
from dotenv import load_dotenv
from logging_setup import setup_logger

logger = setup_logger(__name__)

logger.info("Logger setup done at db.py")

load_dotenv()

# Function to connect to the database
def get_db_connection():
    try:
        logger.info("Database connection made successfully at db.py")
        return connection.connect(
            host=os.getenv("DB_HOST"),
            database=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            passwd=os.getenv("DB_PASSWORD"),
            use_pure=True
        )
    except Exception as e:
        logger.error(f"There was an error connecting to database at db.py: {e}")

# Function to import the dataframe from the database
def fetch_dataframe(query: str) -> pd.DataFrame:
    try:
        mydb = get_db_connection()
        df = pd.read_sql(query, mydb)
        mydb.close()
        logger.info("Query executed successfully at db.py")
        return df
    except Exception as e:
        logger.error(f"There was an error while fetching dataframe at db.py: {e}")
        return pd.DataFrame()
