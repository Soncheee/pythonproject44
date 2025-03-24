import pytest

from src.generators import (card_number_generator, filter_by_currency,
                            transaction_descriptions, transactions)


@pytest.mark.parametrize("valute, expected_count", [
    ("USD", 3),
    ("RUB", 2),
    ("EUR", 0)
])


def test_filter_by_currency(valute, expected_count):
    filtered = list(filter_by_currency(transactions, valute))
    assert len(filtered) == expected_count
    assert filter(lambda t: t["operationAmount"]["currency"]["code"] == valute,
                  transactions)


def test_transaction_descriptions():
    descriptions = list(transaction_descriptions(transactions))
    assert len(descriptions) == 5
    assert all(description in [t["description"] for t in transactions]
               for description in descriptions)


@pytest.mark.parametrize("start, stop, expected", [
    (1, 1, ["0000 0000 0000 0001"]),
    (10, 10, ["0000 0000 0000 0010"]),
    (9999999999999998, 9999999999999999,
     ["9999 9999 9999 9998", "9999 9999 9999 9999"])
])

def test_card_number_generator(start, stop, expected):

    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected

