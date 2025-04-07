# file_processor.py
import csv
from typing import Dict, List

import pandas as pd


def read_transactions_from_csv(file_path: str) -> List[Dict]:
    '''функция для считывания финансовых операций из CSV'''
    transactions = []

    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                # Преобразуем пустые строки в None
                transaction = {key: (value if value else None)
                               for key, value in row.items()}
                transactions.append(transaction)
        return transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении CSV файла: {str(e)}")
        return []


def read_transactions_from_excel(file_path: str) -> List[Dict]:
    '''функция для считывания финансовых операций из Excel'''
    try:
        # Читаем Excel файл с помощью pandas
        df = pd.read_excel(file_path)

        # Преобразуем DataFrame в список словарей
        transactions = []
        for record in df.to_dict('records'):
            # Преобразуем NaN в None и приводим ключи к строкам
            transaction = {str(key): (None if pd.isna(value) else str(value))
                           for key, value in record.items()}
            transactions.append(transaction)
        return transactions

    except FileNotFoundError:
        print(f"Ошибка: Файл {file_path} не найден")
        return []
    except Exception as e:
        print(f"Ошибка при чтении Excel файла: {str(e)}")
        return []
