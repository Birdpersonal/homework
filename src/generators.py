from typing import Iterator, Generator

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(list_dict: list[dict], currency: str) -> Iterator[dict]:
    """Функция возвращает итератор с транзакциями"""

    found_any = False

    for i in list_dict:
        operation_amount = i.get("operationAmount", {})
        currency_info = operation_amount.get("currency", {})
        currency_name = currency_info.get("name")

        if currency_name == currency:
            found_any = True
            yield i

    if not found_any:
        print("нет данных по операциям")


usd_transactions = filter_by_currency(transactions, "руб.")
try:
    for _ in range(2):
        print(next(usd_transactions))
except StopIteration:
    print("нет данных")


def transaction_descriptions(list_dict: list[dict]) -> Generator[str]:
    """Функция возвращает описание операций"""
    try:
        for i in list_dict:
            yield i["description"]
    except (KeyError, StopIteration):
        print("нет данных по операциям")


try:
    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))
except StopIteration:
    print("нет данных")


def card_number_generator(start: int, stop: int) -> Generator:
    """Функция генерирует номера банковских крат"""
    for i in range(start, stop + 1):
        gen_card_number = str(i).zfill(16)
        yield f"{gen_card_number[:4]} {gen_card_number[4:8]} {gen_card_number[8:12]} {gen_card_number[12:]}"


try:
    for card_number in card_number_generator(1, 5):
        print(card_number)
except StopIteration:
    print("нет данных")
