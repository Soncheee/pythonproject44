import pytest

from src import widget


@pytest.mark.parametrize(
    "card_or_account_info,expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_mask_account_card(card_or_account_info, expected):
    assert widget.mask_account_card(card_or_account_info) == expected


@pytest.mark.parametrize(
    "date,expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2025-02-10T02:26:18.671407", "10.02.2025"),
    ],
)
def test_get_date(date, expected):
    assert widget.get_date(date) == expected

