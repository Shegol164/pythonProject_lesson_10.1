import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions) -> None:
    generator = filter_by_currency(transactions)
    assert next(generator)


def test_filter_by_currency_error() -> None:
    with pytest.raises(TypeError, match ="Данный код валюты отсутствует"):
        list(filter_by_currency([{"operationAmount": {"currency": {"code": ""}}}], " "))


def test_transaction_descriptions(transactions) -> None:
    generator = transaction_descriptions(transactions)
    assert list(generator)


def test_transaction_descriptions_error() -> None:
    with pytest.raises(TypeError, match="Данные отсутствуют"):
        list(transaction_descriptions([{"": ""}]))


def test_card_number_generator() -> None:
    generator = card_number_generator(1, 11)
    assert list(generator)


def test_card_number_generator_error() -> None:
    with pytest.raises(IndexError, match ="Неправильный ввод данных"):
        list(card_number_generator(5, 0))