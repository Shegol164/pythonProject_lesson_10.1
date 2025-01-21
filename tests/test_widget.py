import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card(expected_mask_account_card: str) -> str:
    assert mask_account_card("Visa1111111111111111") == expected_mask_account_card


def test_mask_account_card_min(expected_mask_account_card_min: str) -> str:
    assert mask_account_card("Visa1111111111") == expected_mask_account_card_min


def test_mask_account_card_max(expected_mask_account_card_max: str) -> str:
    assert mask_account_card("Visa11111111111111111111") == expected_mask_account_card_max


def test_mask_account_card_zero(expected_mask_account_card_zero: str) -> str:
    assert mask_account_card("") == expected_mask_account_card_zero


def test_mask_account_card_check(expected_mask_account_card_check: str) -> str:
    assert mask_account_card("Счет11111111111111111111") == expected_mask_account_card_check


def test_mask_account_card_check_min(expected_mask_account_card_check_min: str) -> str:
    assert mask_account_card("Счет11111111") == expected_mask_account_card_check_min


def test_mask_account_card_check_max(expected_mask_account_card_check_max: str) -> str:
    assert mask_account_card("Счет111111111111111111111111111111") == expected_mask_account_card_check_max


def test_get_date(expected_get_date: str) -> None:
    assert get_date("2024-03-11T02:26:18.671407") == expected_get_date


def test_get_date_zero(expected_get_date_zero: str) -> None:
    assert get_date("") == expected_get_date_zero


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("Visa1111111111111111", " Visa 11** **** 1111"),
        ("Visa1111111111", " Visa 11** **** 1111"),
        ("Visa11111111111111111111", " Visa 11** **** 1111"),
        ("", "Пустая строка"),
        ("Счет11111111111111111111", " **1111"),
        ("Счет11111111", " **1111"),
        ("Счет111111111111111111111111111111", " **1111"),
    ],
)
def test_mask_account_card_parametrize(string: str, expected_result: str) -> None:
    assert mask_account_card(string) == expected_result


@pytest.mark.parametrize(
    "string, expected_result", [("2024-03-11T02:26:18.671407", "11.03.2024"), ("", "Пустая строка")]
)
def test_get_date_parametrize(string: str, expected_result: str) -> None:
    assert get_date(string) == expected_result
