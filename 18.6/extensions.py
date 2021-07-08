import requests
import json
from config import keys


class ConversionException(Exception):  # класс для отлова ошибок пользователя
    pass


class CryptoConvertor:  # обработка ошибок и запрос с сайта
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        if quote == base:
            raise ConversionException("две одинаковые валюты")

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту {base}")

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionException(f"Не удалось обработать валюту {quote}")

        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException(f"Не удалось обработать количество{amount}")

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}"
                         f"&tsyms={base_ticker}")

        total_base = json.loads(r.content)[base_ticker]

        return total_base * amount
