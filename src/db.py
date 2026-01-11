import sqlite3
import pandas as pd
from pathlib import Path


class SQLiteRepository:
    """
    Репозиторий для работы с SQLite.
    """

    def __init__(self, db_path: Path):
        self.db_path = db_path

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def create_table(self):
        """
        Создаёт таблицу, если она не существует.
        """
        query = """
        CREATE TABLE IF NOT EXISTS crypto_prices (
            coin TEXT,
            currency TEXT,
            price REAL,
            load_date DATE,
            PRIMARY KEY (coin, load_date)
        );
        """
        with self._get_connection() as conn:
            conn.execute(query)

    def data_exists_for_date(self, load_date: str) -> bool:
        """
        Проверяет, есть ли данные за указанную дату.
        """
        query = """
        SELECT 1
        FROM crypto_prices
        WHERE load_date = ?
        LIMIT 1;
        """
        with self._get_connection() as conn:
            result = conn.execute(query, (load_date,))
            return result.fetchone() is not None

    def insert_dataframe(self, df: pd.DataFrame):
        """
        Загружает DataFrame в SQLite.
        """
        with self._get_connection() as conn:
            df.to_sql(
                "crypto_prices",
                conn,
                if_exists="append",
                index=False,
            )
