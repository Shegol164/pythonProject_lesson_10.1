import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_number(expected_mask: str) -> str:
    assert get_mask_card_number("1111111111111111") == expected_mask


def test_mask_card_number_min(expected_mask_min: str) -> str:
    assert get_mask_card_number("1111111111") == expected_mask_min


def test_mask_card_number_max(expected_mask_max: str) -> str:
    assert get_mask_card_number("11111111111111111111") == expected_mask_max


def test_mask_card_number_zero(expected_mask_zero: str) -> str:
    assert get_mask_card_number("") == expected_mask_zero


def test_mask_card_number_letter(expected_mask_letter: str) -> str:
    assert get_mask_card_number("aaaaaaaaaaaaaaaa") == expected_mask_letter


def test_mask_card_number_letter_min(expected_mask_letter_min: str) -> str:
    assert get_mask_card_number("aaaaaaaaaa") == expected_mask_letter_min


def test_mask_card_number_letter_max(expected_mask_letter_max: str) -> str:
    assert get_mask_card_number("aaaaaaaaaaaaaaaa") == expected_mask_letter_max


@pytest.mark.parametrize(
    "string, expected_result",
    [
        ("11111111111111111", "1111 11** **** 1111"),
        ("1111111111", "1111 11** **** 1111"),
        ("11111111111111111111", "1111 11** **** 1111"),
        ("", " ** **** "),
    ],
)
def test_get_mask_card_number(string: str, expected_result: str)->None:
    assert get_mask_card_number(string) == expected_result


def test_get_mask_account(expected_mask_account: str) -> str:
    assert get_mask_account("11111111111111111111") == expected_mask_account


def test_get_mask_account_min(expected_mask_account_min: str) -> str:
    assert get_mask_account("11111111") == expected_mask_account_min


def test_get_mask_account_max(expected_mask_account_max: str) -> str:
    assert get_mask_account("111111111111111111111111111111") == expected_mask_account_max


def test_get_mask_card_number_zero(expected_mask_account_zero: str) -> str:
    assert get_mask_account("") == expected_mask_account_zero


@pytest.mark.parametrize(
    "string, expected_result",
    [("1111111111111111", "**1111"), ("1111111111", "**1111"), ("11111111111111111111", "**1111"), ("", "**")],
)
def test_mask_account(string, expected_result):
    assert get_mask_account(string) == expected_result
