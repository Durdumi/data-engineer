from pathlib import Path

# Базовая директория проекта
BASE_DIR = Path(__file__).resolve().parents[1]

# База данных
DB_PATH = BASE_DIR / "data" / "database.sqlite"

# CoinGecko API
COINGECKO_API_URL = "https://api.coingecko.com/api/v3/simple/price"

# Какие монеты и валюты забираем
COINS = ["bitcoin", "ethereum"]
VS_CURRENCY = "usd"
