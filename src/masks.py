def get_mask_card_number(card_number: str) -> str:
    """Функция на вход принимает номер карты и выдает маску.
    Пример 7000792289606361 # входной аргумент
    7000 79** **** 6361 # выход функции
    """
    if not card_number:
        return "Пустая строка"
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция на вход принимает номер счета и выдает маску.
    Пример
    73654108430135874305 # входной аргумент
    **4305 # выход функции
    """
    if not account:
        return "Пустая строка"
    return f"**{account[-4:]}"
