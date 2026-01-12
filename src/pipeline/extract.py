import requests
from src.logger import logger

API_URL = "https://jsonplaceholder.typicode.com/users"  # пример API


def extract_data() -> list[dict]:
    logger.info(f"Extract: получение данных из API {API_URL}")
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.json()
        # упрощаем под наш пайплайн
        return [{"id": user["id"], "name": user["name"], "age": 20 + user["id"] % 10} for user in data]
    except Exception as e:
        logger.exception("Extract: ошибка при получении данных с API")
        return []
