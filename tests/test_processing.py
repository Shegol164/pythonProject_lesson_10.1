from typing import Dict, List

from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_executed(expected_filter_by_state_executed: List[Dict]) -> List[Dict]:
    assert filter_by_state(expected_filter_by_state_executed) == expected_filter_by_state_executed


def test_filter_by_state_canceled(expected_filter_by_state_canceled: List[Dict]) -> List[Dict]:
    assert filter_by_state(expected_filter_by_state_canceled, "CANCELED") == expected_filter_by_state_canceled


def test_filter_by_state_zero(expected_filter_by_state_zero: List[Dict]) -> str:
    assert filter_by_state(data_list=[]) == expected_filter_by_state_zero


def test_sort_by_date(expected_sort_by_date: List[Dict]) -> List[Dict]:
    assert sort_by_date(expected_sort_by_date) == expected_sort_by_date


def test_sort_by_date_false(expected_sort_by_date_false: List[Dict]) -> List[Dict]:
    assert sort_by_date(expected_sort_by_date_false, False) == expected_sort_by_date_false


def test_sort_by_date_zero(expected_sort_by_date_zero: List[Dict]) -> str:
    assert sort_by_date(data_list=[]) == expected_sort_by_date_zero
