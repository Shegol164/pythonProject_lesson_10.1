def filter_by_state(dictionary: list[dict]) -> list[dict]:
    """Функция принимает список словарей и возвращает список словарей отсортированный по значению ключа 'EXECUTED'"""
    filter_argument = "EXECUTED"
    new_dictionary_1 = []
    for i in dictionary:
        if i["state"] == filter_argument:
            new_dictionary_1.append(i)
    return new_dictionary_1


def sort_by_date(dictionary: list[dict]) -> list[dict]:
    """Функция принимает на вход словарь и аргумент сортировки, сортирует по дате, по возрастанию"""
    sort_argument = "date"
    sorted_dictionary = sorted(dictionary, key=lambda x: x[sort_argument])
    return sorted_dictionary
