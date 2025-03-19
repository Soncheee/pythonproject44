import json
import logging
import os

logger = logging.getLogger("utils")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("..\\logs\\utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transaction(json_file_path):
    """Принимает путь до json файла и выводит его списком"""
    logger.info("Проверка что файл есть на пути")
    if os.path.exists(json_file_path):
        try:
            with open(json_file_path, "r", encoding="utf-8") as file:
                logger.info("Открываем и читаем файл")
                transactions = json.load(file)
                logger.info("Проверка что файл имеет нужный тип")
                if isinstance(transactions, list):
                    return transactions
                else:
                    logger.error("Файл находится не в списке")
                    return []
        except (json.JSONDecodeError, TypeError):
            logger.error("Ошибка при чтении json файла")
            return []
    else:
        logger.error(f"Файл по пути {json_file_path} не существует")
        return []


get_transaction("..\\data\\operations.json")
