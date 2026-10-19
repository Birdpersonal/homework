from typing import Any


def filter_by_state(list_dick: list, state: str = "EXECUTED") -> list:
    """Фильтрация операций по ключу"""
    new_list_dick = []
    for i in list_dick:
        if i["state"] == state:
            new_list_dick.append(i)
    return new_list_dick


if __name__ == "__main__":
    result = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(result, "CANCELED"))


def sort_by_date(list_dickt: list[Any], reverse: bool = True) -> list[Any]:
    """Отсортировывает список по дате"""
    revers = reverse
    sorted_list = sorted(list_dickt, key=lambda x: x["date"], reverse=revers)
    return sorted_list


if __name__ == "__main__":
    resalt = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(sort_by_date(resalt, False))
