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
    only_executed = filter_by_state(data_list)
    only_canceled = filter_by_state(data_list, "CANCELED")

# Пример использования sort_by_date
    sorted_descending = sort_by_date(data_list)
    sorted_acscending = sort_by_date(data_list, False)
