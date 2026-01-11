import logging

from api_client import CoinGeckoClient
from data_processor import process_crypto_data
from db import SQLiteRepository
from config import DB_PATH


def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def main():
    setup_logging()
    logger = logging.getLogger(__name__)

    logger.info("Запуск пайплайна загрузки данных")

    repo = SQLiteRepository(DB_PATH)
    repo.create_table()

    client = CoinGeckoClient()
    raw_data = client.fetch_prices()

    df = process_crypto_data(raw_data)

    load_date = str(df["load_date"].iloc[0])

    if repo.data_exists_for_date(load_date):
        logger.warning("Данные за сегодня уже загружены. Пропускаем.")
        return

    repo.insert_dataframe(df)
    logger.info("Данные успешно загружены в SQLite")


if __name__ == "__main__":
    main()
