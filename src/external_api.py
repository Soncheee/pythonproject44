import os
import requests
from dotenv import load_dotenv


def get_transaction_amount(transaction_info, currency="RUB"):
    '''Функция возвращает сумму в рублях, если сумма указана в рублях - возвращает сразу, если в дргой валюте,
     то переводит в рубли с текущим курсом'''
    code = transaction_info.get("operationAmount").get("currency").get("code")
    amount = transaction_info.get("operationAmount").get("amount")
    if code == currency:
        return amount
    else:
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={currency}&from={code}&amount={amount}"
        print(url)
        load_dotenv()
        API_KEY = os.getenv("API_KEY")
        headers = {"apikey": f"{API_KEY}"}
        response = requests.get(url, headers=headers)
        return response.json()["result"]


transaction = {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
        "amount": "31957.58",
        "currency": {"name": "руб.", "code": "USD"},
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589",
}

print(get_transaction_amount(transaction))
