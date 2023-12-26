import json
from dateutil import parser


def read_operations(file):
    """
    Открываем файл и загружаем данные в формате JSON
    """
    with open(file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def get_first_successful_operations(operations_data, count=5):
    """
    Фильтруем операции по состоянию 'EXECUTED' и возвращаем
    указанное количество первых успешных операций
    """
    successful_operations = [
        operation for operation in operations_data
        if operation.get('state') == 'EXECUTED'
    ]
    first_successful = successful_operations[:count]
    return first_successful


def format_date(date_str):
    """
    Преобразует строку даты в формате 'dd.mm.YYYY'.
    """
    return parser.parse(date_str).strftime("%d.%m.%Y")


def mask_card_number(card_number):
    """
    Маскирует номер карты, скрывая часть цифр.
    """
    visible = card_number.split(' ')[-1]
    return card_number.replace(visible, f"{visible[:4]} {visible[4:6]}** **** {visible[-4:]}")


def mask_account_number(account_number):
    """
    Маскирует номер счета, показывая только последние 4 цифры.
    """
    return f"**{account_number[-4:]}"


def get_masked_data(operation):
    """
    Извлекает маскированные данные из операции и выводит их.
    """
    date = format_date(operation['date'])
    description = operation['description']

    if 'from' not in operation and 'to' in operation:
        to_where = mask_account_number(operation['to'])
        print(f"{date} {description}")
        print(f"Счет {to_where}")
        print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
    else:
        from_where = mask_card_number(operation.get('from', ''))
        to_where = mask_account_number(operation['to'])
        amount = operation['operationAmount']['amount']
        currency = operation['operationAmount']['currency']['name']
        print(f"{date} {description}")
        print(f"{from_where} -> Счет {to_where}")
        print(f"{amount} {currency}\n")


file_path = 'operations.json'
operations_data = read_operations(file_path)
successful_operations = get_first_successful_operations(operations_data)

for operation in successful_operations:
    get_masked_data(operation)
