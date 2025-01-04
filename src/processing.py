def filter_by_state(dictionary: list[dict[str, any]]) -> list[dict[str, any]]:
    """Функция возвращает список отсортированный по значению ключа 'EXECUTED' и 'CANCELED'"""
    new_dictionary_1 = []
    new_dictionary_2 = []
    for i in dictionary:
        if i["state"] == "EXECUTED":
            new_dictionary_1.append(i)
    for i in dictionary:
        if i["state"] == "CANCELED":
            new_dictionary_2.append(i)
    return f"{new_dictionary_1}\n{new_dictionary_2}"


def sort_by_date(dictionary: list[dict[str, any]]) -> list[dict[str, any]]:
    """Функция принимает на вход словарь и сортирует по дате по убыванию"""
    sorted_dictionary = sorted(dictionary, key=lambda x: x["date"], reverse=True)
    return sorted_dictionary
