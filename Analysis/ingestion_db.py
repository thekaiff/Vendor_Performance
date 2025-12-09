# %pip install pandas
# %pip install sqlalchemy

import pandas as pd 
import os
from sqlalchemy import create_engine
import logging
import time

db_file = os.path.abspath(os.path.join(os.path.dirname(__file__), 'Inventory.db'))
engine = create_engine(f"sqlite:///{db_file}")

def ingest_db(data, table_name, con=None, chunksize=50000, if_exists="append"):
    """Ingest CSV file(s) or a pandas DataFrame into a SQL table.

    Parameters
    - data: path to a CSV file (string / PathLike) or a pandas.DataFrame
    - table_name: target table name in the DB
    - con: SQLAlchemy Engine or sqlite3.Connection. If None, module-level `engine` is used.
    - chunksize: used when `data` is a CSV path to read in chunks
    - if_exists: passed to `DataFrame.to_sql`

    Backwards compatible with previous signature where the third positional
    argument was an engine.
    """
    # maintain backward compatibility: if caller passed engine as positional arg
    if con is None:
        con = engine

    # If a DataFrame is provided, write it directly
    if isinstance(data, pd.DataFrame):
        data.to_sql(table_name, con=con, if_exists=if_exists, index=False)
        return

    # If a path (string / PathLike) is provided, stream it in chunks
    if isinstance(data, (str, os.PathLike)):
        for chunk in pd.read_csv(data, chunksize=chunksize):
            chunk.to_sql(table_name, con=con, if_exists=if_exists, index=False)
        return

    raise ValueError("`data` must be a file path (string/PathLike) or a pandas DataFrame")

def load_raw_data():
    start = time.time()

    data_path = "D:/kaif2/04_Projects/Data_Analyst/Python/Vendor_Performance/Data"

    for file in os.listdir(data_path):
        if file.endswith(".csv"):
            file_path = os.path.join(data_path, file)
            logging.info(f"Ingesting {file} in db")

            # send file path, not whole df
            ingest_db(file_path, file[:-4], engine)

    end = time.time()
    total_time = (end-start)/60
    logging.info("--------------Ingestion Completed--------------")
    logging.info(f"Total Time Taken: {total_time} minutes")


if __name__ == "__main__":
    logging.basicConfig(
        filename = "G:/Kaif/Code/Logs/Ingestion_DB.log",
        level= logging.DEBUG,
        format= "%(asctime)s - %(levelname)s - %(message)s",
        filemode= "a"
    )

    load_raw_data()
