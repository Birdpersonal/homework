import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "value, expected",
    [
        ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Flatinum 8990922113665229", "Такой карты нет"),
        ("Счет 736541084301358745", "Неточное количество цифр"),
        ("Visa Classic 68319824767658", "Неточное количество цифр"),
    ],
)
def test_mask_account_card(value: str, expected: str) -> None:
    assert mask_account_card(value) == expected


@pytest.mark.parametrize(
    "value, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2026-01-13T12:16:12.24657", "13.01.2026"),
        ("2012-12-24T12:14:12.26896", "24.12.2012"),
        ("", "Введите дату"),
    ],
)
def test_get_date(value: str, expected: str) -> None:
    assert get_date(value) == expected
