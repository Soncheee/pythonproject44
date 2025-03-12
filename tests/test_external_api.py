import os
from unittest.mock import patch

from dotenv import load_dotenv

from src.external_api import get_transaction_amount


@patch("requests.get")
def test_get_transaction_amount_mock(mock_get):
    '''Тест для конвертации валюты с использованием Mock и patch.'''
    mock_get.return_value.json.return_value = {
        "success": True,
        "info": "some_info",
        "result": "1000",
    }
    assert (
        get_transaction_amount(
            {
                "id": 490100847,
                "state": "EXECUTED",
                "date": "2018-12-22T02:02:49.564873",
                "operationAmount": {
                    "amount": "56516.63",
                    "currency": {"name": "USD", "code": "USD"},
                },
            }
        )
        == "1000"
    )
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=56516.63",
        headers={"apikey": API_KEY},
    )


def test_get_transaction_amount():
    assert (
        get_transaction_amount(
            {
                "id": 441945886,
                "state": "EXECUTED",
                "date": "2019-08-26T10:50:58.294041",
                "operationAmount": {
                    "amount": "31957.58",
                    "currency": {"name": "руб.", "code": "RUB"},
                },
                "description": "Перевод организации",
                "from": "Maestro 1596837868705199",
                "to": "Счет 64686473678894779589",
            }
        )
        == "31957.58"
    )
