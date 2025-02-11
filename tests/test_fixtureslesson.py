import pytest

from src.fixtureslesson import reverse_string
from src.fixtureslesson import finder

def test_reverse_numbers(numbers):
    assert reverse_string("123") == numbers


def test_reverse_letters(letters):
    assert reverse_string("янемилтебе") == letters


@pytest.mark.parametrize('value, expected', [('123', '321'), ('янемилтебе','ебетлименя'), ('654','456')])
def test_reverse_string(value, expected):
    assert reverse_string(value) == expected


def test_finder_basic():
    assert finder([1, "2", [], {}, ("3",)], int) == 1
    assert finder([1, "2", [], {}, ("3",), 3], int) == 2


def test_finder_zero():
    assert finder([1, 2, [], {}, ("3",), 3], str) == 0


def test_finder_empty():
    assert finder([], str) == 0


def test_finder_not_list():
    assert finder(123, int) == 0


