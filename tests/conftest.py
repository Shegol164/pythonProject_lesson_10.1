import pytest


@pytest.fixture
def mask():
    return '1111 11** **** 1111'


@pytest.fixture
def mask_min():
    return '1111 11** **** 1111'


@pytest.fixture
def mask_max():
    return '1111 11** **** 1111'


@pytest.fixture
def mask_zero():
    return ' ** **** '


@pytest.fixture
def mask_letter():
    return 'aaaa aa** **** aaaa'


@pytest.fixture
def mask_letter_min():
    return 'aaaa aa** **** aaaa'


@pytest.fixture
def mask_letter_max():
    return 'aaaa aa** **** aaaa'


@pytest.fixture
def mask_account():
    return '**1111'


@pytest.fixture
def mask_account_zero():
    return '**'
