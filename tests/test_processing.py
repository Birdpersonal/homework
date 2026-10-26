from src.processing import filter_by_state, sort_by_date


def test_filter_by_state(state, answer_state):
    assert filter_by_state(state,"CANCELED") == answer_state

# def test_filter_not_state(state_1, answer_state_1):
#     assert filter_by_state(state_1, "CANCELED") == answer_state_1

def test_sort_by_date(date, answer_date):
    assert sort_by_date(date, False) == answer_date

def test_sort_by_date_f(date, answer_date_1):
    assert sort_by_date(date, True) == answer_date_1