# Учебный проект по Python

## Описание:
Данный учебный проект содержит материалы заданий уроков:
- 9.1 Poetry. Оформление кода
- 9.2 Осовы Git
- 10.1 Продвинутый Git

## Установка:
   1. Клонируйте репозиторий:
https://github.com/Shegol164/pythonProject_lesson_10.1.git
   2. Перейдите в директорию проекта:
 pythonProject_lesson_10.1

## Использование:
Примеры использования функций:
from src.processing import filter_by_state, sort_by_date

# Пример использования filter_by_state
print(
    filter_by_state(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)

# Пример использования sort_by_date
print(
    sort_by_date(
        [
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        ]
    )
)
