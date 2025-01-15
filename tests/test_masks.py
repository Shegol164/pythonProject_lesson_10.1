from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_account(mask):
    assert get_mask_card_number('1111111111111111') == mask


def test_get_mask_card_number(mask_account):
    assert get_mask_account('11111111111111111111') == mask_account
