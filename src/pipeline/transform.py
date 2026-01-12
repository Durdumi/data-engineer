from src.logger import logger


def transform_data(data: list[dict]) -> list[dict]:
    logger.info("Transform: начало трансформации")

    transformed = [
        row for row in data if row["age"] >= 18
    ]

    logger.info(
        f"Transform: {len(transformed)} записей после фильтрации"
    )
    return transformed
