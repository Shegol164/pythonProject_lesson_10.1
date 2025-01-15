from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_mask_card_number(mask):
    assert get_mask_card_number('1111111111111111') == mask


def test_mask_card_number_min(mask_min):
    assert get_mask_card_number('1111111111') == mask_min


def test_mask_card_number_max(mask_max):
    assert get_mask_card_number('11111111111111111111') == mask_max


def test_mask_card_number_zero(mask_zero):
    assert get_mask_card_number('') == mask_zero


def test_mask_card_number_letter(mask_letter):
    assert get_mask_card_number('aaaaaaaaaaaaaaaa') == mask_letter


def test_mask_card_number_letter_min(mask_letter_min):
    assert get_mask_card_number('aaaaaaaaaa') == mask_letter_min


def test_mask_card_number_letter_max(mask_letter_max):
    assert get_mask_card_number('aaaaaaaaaaaaaaaa') == mask_letter_max


def test_get_mask_account(mask_account):
    assert get_mask_account('11111111111111111111') == mask_account


def test_get_mask_card_number_zero(mask_account_zero):
    assert get_mask_account('') == mask_account_zero
