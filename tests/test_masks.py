from typing import Any

import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "value, expected",
    [
        (8426482346371948, "8426 48** **** 1948"),
        (8422346371948, "Неккоректное количество цифр"),
        ("84223463719as48", "Введите номер карты без букв"),
        ("", "Введите число"),
    ],
)
def test_get_mask_card_number(value: Any, expected: str) -> None:
    assert get_mask_card_number(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        (73654108430135874305, "**4305"),
        (8422346371948, "Неккоректное количество цифр"),
        ("73654108430as5874305", "Введите номер карты без букв"),
        ("", "Введите число"),
    ],
)
def test_get_mask_account(value: Any, expected: Any) -> None:
    assert get_mask_account(value) == expected
