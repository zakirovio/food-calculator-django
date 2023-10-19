import sqlite3
import pandas as pd
from sqlalchemy import create_engine
from config import settings


def import_to_mysql(url, excel_table_path: str, db_table: str):
    engine = create_engine(url, echo=False)
    df = pd.read_excel(excel_table_path)
    df.to_sql(name=db_table, if_exists='append', con=engine, index=False)
    print('[INFO] OK')


if __name__ == '__main__':
    is_import = True
    if is_import:
        # Import categories
        import_to_mysql(url=settings.MYSQL_URL, excel_table_path=f"{settings.BASE_DIR}/data/categories.xlsx",
                        db_table="calculator_categories")
        # Import products
        import_to_mysql(url=settings.MYSQL_URL, excel_table_path=f"{settings.BASE_DIR}/data/products.xlsx",
                        db_table="calculator_products")

