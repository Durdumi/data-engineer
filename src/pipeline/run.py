from src.pipeline.extract import extract_data
from src.pipeline.transform import transform_data
from src.pipeline.load import load_data
from src.logger import logger


def run_pipeline() -> None:
    logger.info("Pipeline: старт")

    try:
        raw_data = extract_data()
        transformed_data = transform_data(raw_data)
        load_data(transformed_data)

    except Exception:
        logger.exception("Pipeline: ошибка выполнения")
        raise

    logger.info("Pipeline: завершён успешно")
