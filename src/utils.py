import json
import os


def get_transaction(json_file_path):
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, "r", encoding="utf-8") as file:
                transactions = json.load(file)
                if isinstance(transactions, list):
                    return transactions
                else:
                    return []
        except (json.JSONDecodeError, TypeError):
            return []
    else:
        return []


