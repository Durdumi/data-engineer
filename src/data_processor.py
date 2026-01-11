import pandas as pd
from datetime import datetime


def process_crypto_data(raw_data: dict) -> pd.DataFrame:
    """
    Преобразует сырые данные API в pandas DataFrame.
    """
    records = []

    load_date = datetime.utcnow().date()

    for coin, values in raw_data.items():
        records.append(
            {
                "coin": coin,
                "currency": "usd",
                "price": values["usd"],
                "load_date": load_date,
            }
        )

    df = pd.DataFrame(records)
    return df
