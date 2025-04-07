# main.py
from file_processor import (read_transactions_from_csv,
                            read_transactions_from_excel)


def main():
    csv_file_path = "src/transactions.csv"
    csv_transactions = read_transactions_from_csv(csv_file_path)

    print("Первые 2 транзакции из CSV:")
    for transaction in csv_transactions[:2]:
        print(transaction)

    excel_file_path = "src/transactions_excel.xlsx"
    excel_transactions = read_transactions_from_excel(excel_file_path)

    print("\nПервые 2 транзакции из Excel:")
    for transaction in excel_transactions[:2]:
        print(transaction)


if __name__ == "__main__":
    main()
