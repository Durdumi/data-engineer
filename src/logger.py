import logging
from src.config import config


def setup_logger() -> logging.Logger:
    logger = logging.getLogger(config.app_name)
    logger.setLevel(config.log_level)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    )

    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger


logger = setup_logger()
