import csv

import pandas as pd


def reading_file_csv(file_path: str) -> list[dict]:
    """Функция принимает файл csv и возвращает список словарей"""
    with open(file_path, "r", encoding="utf=8") as list_dict:
        reader = csv.DictReader(list_dict)
        return list(reader)


def reading_file_xlsx(file_path: str) -> list[dict]:
    """Функция принимает файл excel и возвращает список словарей"""
    excel_file = pd.read_excel(file_path).to_dict(orient="records")
    return excel_file
