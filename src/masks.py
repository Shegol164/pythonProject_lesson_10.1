import os

from src.logging import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
file_path_1 = os.path.join(current_dir, "../logs", "masks.log")
logger = get_logger("masks", file_path_1)


def get_mask_card_number(card_number: str) -> str:
    """Функция на вход принимает номер карты и выдает маску.
    Пример 7000792289606361 # входной аргумент
    7000 79** **** 6361 # выход функции
    """
    logger.info("Функция  маскирует номер карты по типу 7000 79** **** 6361")
    if not card_number:
        logger.error("Введена пустая строка")
        return "Пустая строка"
    mask_card = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
    logger.info(f"Введен номер карты: {mask_card}")
    return mask_card


def get_mask_account(account: str) -> str:
    """Функция на вход принимает номер счета и выдает маску.
    Пример
    73654108430135874305 # входной аргумент
    **4305 # выход функции
    """
    logger.info("Функция  маскирует номер счета по типу **4305")
    if not account:
        logger.error("Введена пустая строка")
        return "Пустая строка"
    mask_account = f"**{account[-4:]}"
    logger.info(f"Введен номер счета: {mask_account}")
    return mask_account
