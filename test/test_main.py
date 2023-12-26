import os

from utils.main import mask_card_number, format_date, mask_account_number, read_operations


def test_operations():
    """
    Проверка чтения данных из файла
    """
    file_path = os.path.join(os.path.dirname(__file__), 'operations.json')
    operations_data = read_operations(file_path)
    assert len(operations_data) > 0


def test_mask_card_number():
    """
    Проверка маскировки номера карты
    """
    card_number = "1234 5678 9012 3456"
    masked_number = mask_card_number(card_number)
    assert '** **** 3456' in masked_number
    assert '1234 5678' in masked_number


def test_format_date():
    """
    Проверка форматирования даты
    """
    date_str = "2023-12-20T12:00:00Z"
    formatted_date = format_date(date_str)
    assert formatted_date == "20.12.2023"


def test_mask_account_number():
    """
    Проверка маскировки номера счета
    """
    account_number = "1234567890123456"
    masked_number = mask_account_number(account_number)
    assert masked_number == "**3456"
