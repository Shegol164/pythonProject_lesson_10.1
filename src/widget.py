from src.masks import get_mask_account, get_mask_card_number
import datetime


def mask_account_card(card_or_account: str) -> str:
    """
    Функция mask_account_card принимает на вход один из аргументов. Выводит маску. Пример:
    Visa Platinum 7000792289606361 # входной аргумент
    Visa Platinum 7000 79** **** 6361 # выход функции
    Счет 73654108430135874305 # входной аргумент
    Счет **4305 # выход функции
    """
    card_or_account_splitted = card_or_account.split()
    card_or_account_type = " ".join(card_or_account_splitted[:-1])

    if card_or_account.lower().startswith("счет"):
        return f"{card_or_account_type} {get_mask_account(card_or_account_splitted[-1])}"
    else:
        return f"{card_or_account_type} {get_mask_card_number(card_or_account_splitted[-1])}"


def get_date(date: str) -> str:
    """Функция принимает на вход дату в формате 2024-03-11T02:26:18.671407 и возвращает в формате 11.03.2024"""

    now = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
    new_data = now.strftime("%d.%m.%Y")
    return new_data
