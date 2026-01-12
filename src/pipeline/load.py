from src.logger import logger


def load_data(data: list[dict]) -> None:
    logger.info("Load: загрузка данных")

    for row in data:
        logger.info(f"Load: {row}")

    logger.info("Load: загрузка завершена")
