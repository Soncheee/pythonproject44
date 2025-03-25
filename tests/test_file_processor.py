from file_processor import (read_transactions_from_csv,
                            read_transactions_from_excel)
import pandas as pd
from unittest.mock import patch, mock_open


def test_read_transactions_from_csv_success():
    '''Тест для успешного вывода CSV'''
    csv_content = "id;amount;date\n1;100.50;2023-01-01\n2;200.75;2023-01-02"
    with patch('builtins.open', mock_open(read_data=csv_content)):
        result = read_transactions_from_csv('fake_path.csv')

        expected = [
            {'id': '1', 'amount': '100.50', 'date': '2023-01-01'},
            {'id': '2', 'amount': '200.75', 'date': '2023-01-02'}
        ]
        assert result == expected


def test_read_transactions_from_csv_empty_values():
    '''Тест для обработки пустых значений'''
    csv_content = "id;amount;date\n1;;2023-01-01\n2;200.75;"
    with patch('builtins.open', mock_open(read_data=csv_content)):
        result = read_transactions_from_csv('fake_path.csv')

        expected = [
            {'id': '1', 'amount': None, 'date': '2023-01-01'},
            {'id': '2', 'amount': '200.75', 'date': None}
        ]
        assert result == expected


def test_read_transactions_from_csv_file_not_found():
    '''Тест для обработки случая, когда CSV-файл не найден'''
    with patch('builtins.open', side_effect=FileNotFoundError):
        result = read_transactions_from_csv('non_existent.csv')
        assert result == []


@patch('pandas.read_excel')
def test_read_transactions_from_excel_success(mock_read_excel):
    '''Тест для успешного чтения Excel'''
    mock_df = pd.DataFrame({
        'id': [1, 2],
        'amount': [100.50, 200.75],
        'date': ['2023-01-01', '2023-01-02']
    })
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel('fake_path.xlsx')

    expected = [
        {'id': '1', 'amount': '100.5', 'date': '2023-01-01'},
        {'id': '2', 'amount': '200.75', 'date': '2023-01-02'}
    ]
    assert result == expected


@patch('pandas.read_excel')
def test_read_transactions_from_excel_with_nan(mock_read_excel):
    '''Тест обработки NaN в Excel'''
    mock_df = pd.DataFrame({
        'id': [1, 2],
        'amount': [pd.NA, 200.75],
        'date': ['2023-01-01', pd.NA]
    })
    mock_read_excel.return_value = mock_df

    result = read_transactions_from_excel('fake_path.xlsx')

    expected = [
        {'id': '1', 'amount': None, 'date': '2023-01-01'},
        {'id': '2', 'amount': '200.75', 'date': None}
    ]
    assert result == expected


@patch('pandas.read_excel', side_effect=FileNotFoundError)
def test_read_transactions_from_excel_file_not_found(mock_read_excel):
    '''Тест для обработки cлучая ненайденного файла Excel'''
    result = read_transactions_from_excel('non_existent.xlsx')
    assert result == []
