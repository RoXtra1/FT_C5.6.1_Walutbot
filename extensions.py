import requests
import json
from config import keys, headers, payload

class APIException(Exception):
    pass

class AskAPI:
    @staticmethod
    def get_price(base: str, quote: str, amount: str): #не понимаю, зачем в данном случае создание отдельного класса? только чтобы использовать staticmethod? но к чему он тут?
        if base == quote:
            raise APIException(f'При переводе валюты "{base}" в себя же получится то же количество')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не знаю валюту "{base}"')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не знаю валюту "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не понимаю, что за количество "{amount}"?')

        r = requests.request("GET",
                             url=f"https://api.apilayer.com/exchangerates_data/convert?to={keys[quote]}&from={keys[base]}&amount={amount}",
                             headers=headers,
                             data=payload)
        text = json.loads(r.content)['result']
        return float(text)
