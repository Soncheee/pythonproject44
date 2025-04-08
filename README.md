# 13.1 **Домашнее задание**

## Инструменты: *pandas, csv, re, collections, json*

### Добавлен файл *reading_transactions.py*

### Содержит функцию фильтрации списка транзакций по определенному слову в описании:
```
def transactions_search_by_desctiption(dict_list, search_string):
    '''Функция возвращает список с выбранным описанием'''
    pattern = re.compile(search_string, re.IGNORECASE)
    return [transaction for transaction in dict_list if pattern.search(transaction.get('desciption', ''))]
```

### Содержит функцию фильтрации по статусу:
```
def transactions_filter_by_status(dict_list, status):
    '''Фильтрует по статусу'''
    status = status.lower()
    return [transaction for transaction in dict_list if transaction.get('status') == status.lower()]
```

### Содержит функцию подсчета категорий:
```
def transactions_filter_by_category(dict_list, categories):
    '''Функция подсчета категорий'''
    categories = []
    for dictionary in dict_list:
        cat = dictionary.get('category', '')
        categories.append(cat)
    categories_count = Counter(categories)
    return categories_coun
```
