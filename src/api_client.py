import requests
import logging
from typing import Dict

from config import COINGECKO_API_URL, COINS, VS_CURRENCY

logger = logging.getLogger(__name__)


class CoinGeckoClient:
    """
    Клиент для работы с CoinGecko API.
    """

    def fetch_prices(self) -> Dict:
        """
        Получает цены криптовалют.
        """
        params = {
            "ids": ",".join(COINS),
            "vs_currencies": VS_CURRENCY,
        }

        logger.info("Запрос данных из CoinGecko API")
        response = requests.get(COINGECKO_API_URL, params=params, timeout=10)
        response.raise_for_status()

        return response.json()
