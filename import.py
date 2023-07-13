import sqlite3
import pandas as pd


def import_tosqlite3(
        db_path: str,
        table_path: str,
        db_table_name: str,
        sheet_name: bool = None,
        index: bool = False
):

    with sqlite3.connect(db_path) as connect:
        wb = pd.read_excel(table_path, sheet_name=sheet_name)
        for sheet in wb:
            wb[sheet].to_sql(name=db_table_name, if_exists='append', con=connect, index=index)


def import_tomysql():
    ...


if __name__ == '__main__':
    print('[INFO: ...start import.]')
