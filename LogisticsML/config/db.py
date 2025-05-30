from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import os
load_dotenv()

def get_engine():
    return create_engine(f'postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}')

def get_table_entregas():
    return pd.read_sql("SELECT * FROM entregas", con=get_engine())

if __name__ == '__main__':
    # print(get_engine())
    df= get_table_entregas()
    print(df.head())