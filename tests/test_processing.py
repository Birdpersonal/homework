from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(state: list[dict], answer_state: list[dict]) -> None:
    assert filter_by_state(state, "CANCELED") == answer_state


# def test_filter_not_state(state_1, answer_state_1):
#     assert filter_by_state(state_1, "CANCELED") == answer_state_1


def test_sort_by_date(date: list, answer_date: list) -> None:
    assert sort_by_date(date, False) == answer_date


def test_sort_by_date_f(date: list, answer_date_1: list) -> None:
    assert sort_by_date(date, True) == answer_date_1
