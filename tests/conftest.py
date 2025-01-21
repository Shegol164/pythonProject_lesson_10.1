import pytest
from typing import Dict, List, Any


@pytest.fixture
def expected_mask() -> str:
    return "1111 11** **** 1111"


@pytest.fixture
def expected_mask_min() -> str:
    return "1111 11** **** 1111"


@pytest.fixture
def expected_mask_max() -> str:
    return "1111 11** **** 1111"


@pytest.fixture
def expected_mask_zero() -> str:
    return " ** **** "


@pytest.fixture
def expected_mask_letter() -> str:
    return "aaaa aa** **** aaaa"


@pytest.fixture
def expected_mask_letter_min() -> str:
    return "aaaa aa** **** aaaa"


@pytest.fixture
def expected_mask_letter_max() -> str:
    return "aaaa aa** **** aaaa"


@pytest.fixture
def expected_mask_account() -> str:
    return "**1111"


@pytest.fixture
def expected_mask_account_min() -> str:
    return "**1111"


@pytest.fixture
def expected_mask_account_max() -> str:
    return "**1111"


@pytest.fixture
def expected_mask_account_zero() -> str:
    return "**"


@pytest.fixture
def expected_mask_account_card() -> str:
    return " Visa 11** **** 1111"


@pytest.fixture
def expected_mask_account_card_min() -> str:
    return " Visa 11** **** 1111"


@pytest.fixture
def expected_mask_account_card_max() -> str:
    return " Visa 11** **** 1111"


@pytest.fixture
def expected_mask_account_card_zero() -> str:
    return "Пустая строка"


@pytest.fixture
def expected_mask_account_card_check() -> str:
    return " **1111"


@pytest.fixture
def expected_mask_account_card_check_min() -> str:
    return " **1111"


@pytest.fixture
def expected_mask_account_card_check_max() -> str:
    return " **1111"


@pytest.fixture
def expected_get_date() -> str:
    return "11.03.2024"


@pytest.fixture
def expected_get_date_max() -> str:
    return "11.03.2024"


@pytest.fixture
def expected_get_date_zero() -> str:
    return "Пустая строка"


@pytest.fixture
def expected_filter_by_state_executed() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def expected_filter_by_state_canceled() -> List[Dict[str, Any]]:
    return [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def expected_filter_by_state_zero() -> List:
    return []


@pytest.fixture
def expected_sort_by_date() -> List[Dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def expected_sort_by_date_false() -> List[Dict[str, Any]]:
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def expected_sort_by_date_zero() -> List:
    return []
