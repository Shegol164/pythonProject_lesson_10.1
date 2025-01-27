from typing import Any, Dict, Iterable


def filter_by_currency(transactions: Iterable[Dict], currency: str = "USD") -> Iterable[Dict]:
    """Функция которая, принимает на вход список словарей, представляющих транзакции и даёт итератор с валютой 'USD'"""
    for i in transactions:
        if (i["operationAmount"]["currency"]["code"]) == currency:
            yield i
        elif (i["operationAmount"]["currency"]["code"]) == "RUB":
            continue
        elif (i["operationAmount"]["currency"]["code"]) != currency:
            raise TypeError("Данный код валюты отсутствует")


def transaction_descriptions(transactions: Iterable[Dict], argument_key: str = "description") -> Iterable[Dict]:
    """Функция который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for x in transactions:
        if argument_key in x:
            yield x[argument_key]
        elif not x.get(argument_key):
            raise TypeError("Данные отсутствуют")


def card_number_generator(start: int, end: int) -> Any:
    """Функция-генератор которая принимает начальное и конечное значения для генерации диапазона номеров."""
    if start >= end:
        raise IndexError("Неправильный ввод данных")
    for card_list in range(start, end):
        if 1 <= start <= 9999999999999999 or 1 <= end <= 9999999999999999:
            card_number = "".join(f"{card_list:016}" for _ in range(16))
            formatted_card_number = " ".join([card_number[i : i + 4] for i in range(0, 16, 4)])
            yield formatted_card_number
