import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from decouple import Config, RepositoryEnv


def import_to_sqlite3(
        dbpath: str,
        tablepath: str,
        dbtablename: str,
        sheet_name: bool = None,
        index: bool = False
):

    with sqlite3.connect(dbpath) as connect:
        wb = pd.read_excel(tablepath, sheet_name=sheet_name)
        for sheet in wb:
            wb[sheet].to_sql(name=dbtablename, if_exists='append', con=connect, index=index)


def import_to_mysql(
        db_user: Config,
        db_password: Config,
        db_host: Config,
        db_name: Config,
        excel_table_path: str,
        db_table: str,
):
    engine = create_engine(f'mysql://{db_user}:{db_password}@{db_host}/{db_name}', echo=False)
    df = pd.read_excel(excel_table_path)
    df.to_sql(name=db_table, if_exists='append', con=engine, index=False)
    print('[INFO] OK')


if __name__ == '__main__':
    # Check
    isSqllite3 = False
    isMysql = int(input('Type 1 — import to DB; Type 0 — continue: '))

    print('[INFO: ...start import.]')
    if isSqllite3:
        db_path = 'food_db.sqlite3'
        table_path = 'data/categories.xlsx'  # Check
        db_table_name = 'calculator_categories'
        import_to_sqlite3(dbpath=db_path, tablepath=table_path, dbtablename=db_table_name)

    if isMysql:
        config = Config(RepositoryEnv('config/.env'))
        user = config('DB_USER')
        password = config('DB_PASS')
        host = config("DB_HOST")
        name = config('DB_NAME')

        import_to_mysql(
            db_user=user,
            db_password=password,
            db_host=host,
            db_name=name,
            excel_table_path='data/categories.xlsx',  # Check
            db_table='calculator_categories'  # Check
        )
        import_to_mysql(
            db_user=user,
            db_password=password,
            db_host=host,
            db_name=name,
            excel_table_path='data/products.xlsx',  # Check
            db_table='calculator_products'  # Check
        )
