# Учебный проект по Python

## Описание:
Данный учебный проект содержит материалы заданий уроков:
- 9.1 Poetry. Оформление кода
- 9.2 Осовы Git
- 10.1 Продвинутый Git
- 10.2 Тестирование. Pytest
- 11.1 Включения и генераторы

## Установка:
   1. Клонируйте репозиторий:
https://github.com/Shegol164/pythonProject_lesson_10.1.git
   2. Перейдите в директорию проекта:
 pythonProject_lesson_10.1

## Использование:
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    card_number = input()
    account = input()
    print(get_mask_card_number(card_number))
    print(get_mask_account(account))
    
print("#" * 119)

if __name__ == "__main__":
    card_or_account = input()
    date = "2024-03-11T02:26:18.671407"
    print(mask_account_card(card_or_account))
    print(get_date(date))

print("#" * 119)

if __name__ == "__main__":
    data_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    only_executed = filter_by_state(data_list)
    only_canceled = filter_by_state(data_list, "CANCELED")
    sorted_descending = sort_by_date(data_list)
    sorted_acscending = sort_by_date(data_list, False)
    print(only_executed)
    print(only_canceled)
    print(sorted_descending)
    print(sorted_acscending)

print("#" * 119)

if __name__ == "__main__":
    transactions = [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160",
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]

    usd_transactions = filter_by_currency(transactions)
    for transaction in usd_transactions:
        print(transaction)

    descriptions = transaction_descriptions(transactions)
    for description in descriptions:
        print(description)

for card in card_number_generator(1, 11):
    print(card)

print("#" * 119)

# Тесты
Для всех функций написаны подробные тесты в папке tests:
- test_masks
- test_widget
- test_processing 
- test_generators

Протестированы разные сценарий формата ввода и вывода 

Например: test_processing
- def test_filter_by_state_executed(expected_filter_by_state_executed: List[Dict]) -> List[Dict]:
    assert filter_by_state(expected_filter_by_state_executed) == expected_filter_by_state_executed

- def test_filter_by_state_canceled(expected_filter_by_state_canceled: List[Dict]) -> List[Dict]:
    assert filter_by_state(expected_filter_by_state_canceled, "CANCELED") == expected_filter_by_state_canceled

- def test_filter_by_state_zero(expected_filter_by_state_zero: List[Dict]) -> str:
    assert filter_by_state(data_list=[]) == expected_filter_by_state_zero

- def test_sort_by_date(expected_sort_by_date: List[Dict]) -> List[Dict]:
    assert sort_by_date(expected_sort_by_date) == expected_sort_by_date

- def test_sort_by_date_false(expected_sort_by_date_false: List[Dict]) -> List[Dict]:
    assert sort_by_date(expected_sort_by_date_false, False) == expected_sort_by_date_false

- def test_sort_by_date_zero(expected_sort_by_date_zero: List[Dict]) -> str:
    assert sort_by_date(data_list=[]) == expected_sort_by_date_zero

test_generators:
- def test_filter_by_currency(transactions) -> None:
    generator = filter_by_currency(transactions)
    assert next(generator)


- def test_filter_by_currency_error() -> None:
    with pytest.raises(TypeError, match ="Данный код валюты отсутствует"):
        list(filter_by_currency([{"operationAmount": {"currency": {"code": ""}}}], " "))


- def test_transaction_descriptions(transactions) -> None:
    generator = transaction_descriptions(transactions)
    assert list(generator)


- def test_transaction_descriptions_error() -> None:
    with pytest.raises(TypeError, match="Данные отсутствуют"):
        list(transaction_descriptions([{"": ""}]))


- def test_card_number_generator() -> None:
    generator = card_number_generator(1, 11)
    assert list(generator)


- def test_card_number_generator_error() -> None:
    with pytest.raises(IndexError, match ="Неправильный ввод данных"):
        list(card_number_generator(5, 0))