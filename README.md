# Учебный проект по Python

## Описание:
Данный учебный проект содержит материалы заданий уроков:
- 9.1 Poetry. Оформление кода
- 9.2 Осовы Git
- 10.1 Продвинутый Git
- 10.2 Тестирование. Pytest

## Установка:
   1. Клонируйте репозиторий:
https://github.com/Shegol164/pythonProject_lesson_10.1.git
   2. Перейдите в директорию проекта:
 pythonProject_lesson_10.1

## Использование:
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    card_number = input()
    account = input()
    print(get_mask_card_number(card_number))
    print(get_mask_account(account))

if __name__ == "__main__":
    card_or_account = input()
    date = "2024-03-11T02:26:18.671407"
    print(mask_account_card(card_or_account))
    print(get_date(date))

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

# Тесты:
Для всех функций написаны подробные тесты в папке tests:
- test_masks
- test_widget
- test_processing 

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