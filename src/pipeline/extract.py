from src.logger import logger


def extract_data() -> list[dict]:
    logger.info("Extract: получение данных")

    data = [
        {"id": 1, "name": "Alice", "age": 30},
        {"id": 2, "name": "Bob", "age": 17},
        {"id": 3, "name": "Charlie", "age": 25},
    ]

    logger.info(f"Extract: получено {len(data)} записей")
    return data
