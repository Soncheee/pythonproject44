import json
import csv
import pandas as pd
import re
from collections import Counter

def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def load_csv(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return list(csv.DictReader(file))

def load_xlsx(filename):
    df = pd.read_excel(filename)
    return df.to_dict(orient='records')

def transactions_search_by_description(dict_list, search_str):
    '''Функция возвращает список с выбранным описанием'''
    pattern = re.compile(search_str, re.IGNORECASE)
    return [transaction for transaction in dict_list if pattern.search(transaction.get('description', ''))]

def transactions_filter_by_category(dict_list, categories):
    '''Функция подсчета категорий'''
    categories = []
    for dictionary in dict_list:
        cat = dictionary.get('category', '')
        categories.append(cat)
    categories_count = Counter(categories)
    return categories_count

def transactions_filter_by_status(dict_list, status):
    '''Фильтрует по статусу'''
    return [transaction for transaction in dict_list if transaction.get('state') == status.upper()]

def get_transaction_amount(transaction):
    '''Извлекает сумму из вложенной структуры'''
    operation_amount = transaction.get('operationAmount', {})
    amount = operation_amount.get('amount', '')
    currency = operation_amount.get('currency', {}).get('name', '')
    return f"{amount} {currency}"

def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    file_choice = input("Ваш выбор: ")
    if file_choice == '1':
        filename = input("Введите имя JSON-файла: ")
        transactions = load_json(filename)
    elif file_choice == '2':
        filename = input("Введите имя CSV-файла: ")
        transactions = load_csv(filename)
    elif file_choice == '3':
        filename = input("Введите имя XLSX-файла: ")
        transactions = load_xlsx(filename)
    else:
        print("Неверный выбор.")
        return

    print(f"Для обработки выбраны транзакции из файла: {filename}")

    valid_statuses = ['executed', 'canceled', 'pending']
    while True:
        status = input(
            "Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтрации статусы: EXECUTED, CANCELED, PENDING: ")
        if status.lower() in valid_statuses:
            break
        else:
            print(f"Статус операции '{status}' недоступен.")

    filtered_transactions = transactions_filter_by_status(transactions, status)

    print(f"Операции отфильтрованы по статусу: {status.upper()}")

    sort_choice = input("Отсортировать операции по дате? Да/Нет: ").strip().lower()
    if sort_choice == 'да':
        sort_order = input("Отсортировать по возрастанию или по убыванию? ").strip().lower()
        reverse = sort_order == 'по убыванию'
        filtered_transactions.sort(key=lambda x: x.get('date', ''), reverse=reverse)

    currency_choice = input("Выводить только рублевые транзакции? Да/Нет: ").strip().lower()
    if currency_choice == 'да':
        filtered_transactions = [transaction for transaction in filtered_transactions if
                                 'RUB' in get_transaction_amount(transaction)]

    search_choice = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет: ").strip().lower()
    if search_choice == 'да':
        search_str = input("Введите слово для поиска в описаниях: ")
        filtered_transactions = transactions_search_by_description(filtered_transactions, search_str)

    if filtered_transactions:
        print("Распечатываю итоговый список транзакций...")
        print(f"Всего банковских операций в выборке: {len(filtered_transactions)}")
        for transaction in filtered_transactions:
            print(f"{transaction.get('date')} {transaction.get('description')}")
            print(f"Сумма: {get_transaction_amount(transaction)}")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")

main()
