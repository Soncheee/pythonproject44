import pytest

from src.decorators import divide, log, my_function


def test_divide_exception_log():
    '''Вызов ошибок для функций my_function и divide'''
    with pytest.raises(TypeError):
        my_function((1, 2), {})
    with pytest.raises(ValueError):
        divide(1, 0)
