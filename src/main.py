from src.logger import logger
from src.pipeline.run import run_pipeline


def main():
    logger.info("Application start")
    run_pipeline()
    logger.info("Application end")


if __name__ == "__main__":
    main()
