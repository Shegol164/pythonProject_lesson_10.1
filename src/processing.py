from typing import Dict, List


def filter_by_state(data_list: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключ"""
    new_dictionary = []
    for i in data_list:
        if i["state"] == state:
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(data_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """Функция принимает список словарей и параметр сортировки(по умолчанию "True" — 'CANCELED').
    Функция возвращает новый список, отсортированный по дате(date)"""
    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
