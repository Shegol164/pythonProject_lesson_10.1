from typing import Dict, List, Any


def filter_by_state(data_list: List[Dict], state: str = "EXECUTED") -> List[Dict[str,str]]:
    """Принимает список словарей и ключ: state (по умолчанию 'EXECUTED').
    Возвращает новый список словарей, содержащий словари соответствующих ключ"""
    if not data_list:
        return []
    new_dictionary = []
    for i in data_list:
        if i["state"] == state:
            new_dictionary.append(i)
    return new_dictionary


def sort_by_date(data_list: List[Dict], reverse: bool = True) -> List[Dict[str,Any]]:
    """Функция принимает список словарей и параметр сортировки(по умолчанию "True" — 'CANCELED').
    Функция возвращает новый список, отсортированный по дате(date)"""
    if not data_list:
        return []
    return sorted(data_list, key=lambda x: x["date"], reverse=reverse)
