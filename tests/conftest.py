import pytest


@pytest.fixture
def expected_mask():
    return '1111 11** **** 1111'


@pytest.fixture
def expected_mask_min():
    return '1111 11** **** 1111'


@pytest.fixture
def expected_mask_max():
    return '1111 11** **** 1111'


@pytest.fixture
def expected_mask_zero():
    return ' ** **** '


@pytest.fixture
def expected_mask_letter():
    return 'aaaa aa** **** aaaa'


@pytest.fixture
def expected_mask_letter_min():
    return 'aaaa aa** **** aaaa'


@pytest.fixture
def expected_mask_letter_max():
    return 'aaaa aa** **** aaaa'


@pytest.fixture
def expected_mask_account():
    return '**1111'


@pytest.fixture
def expected_mask_account_min():
    return '**1111'


@pytest.fixture
def expected_mask_account_max():
    return '**1111'


@pytest.fixture
def expected_mask_account_zero():
    return '**'


@pytest.fixture
def expected_mask_account_card():
    return ' Visa 11** **** 1111'


@pytest.fixture
def expected_mask_account_card_min():
    return ' Visa 11** **** 1111'


@pytest.fixture
def expected_mask_account_card_max():
    return ' Visa 11** **** 1111'


@pytest.fixture
def expected_mask_account_card_zero():
    return "Пустая строка"


@pytest.fixture
def expected_mask_account_card_check():
    return ' **1111'


@pytest.fixture
def expected_mask_account_card_check_min():
    return ' **1111'


@pytest.fixture
def expected_mask_account_card_check_max():
    return ' **1111'


@pytest.fixture
def expected_get_date():
    return '11.03.2024'


@pytest.fixture
def expected_get_date_max():
    return '11.03.2024'


@pytest.fixture
def expected_get_date_zero():
    return "Пустая строка"
