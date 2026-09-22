from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(num_namber: str) -> str:
    """Функция обрабатывает информацию о счетах и картах"""
    letter = num_namber.split()
    nums = letter[-1]
    name = " ".join(letter[:-1])
    if name in ["Visa Platinum", "Visa Classic","Visa Platinum","Visa Gold" "MasterCard", "Maestro"]:
        result = get_mask_card_number(int(nums))
    elif name == "Счет":
        result = get_mask_account(int(nums))
    else:
        result = ""

    return f"{name} {result}"


if __name__ == "__main__":
    print(mask_account_card("Счет 64686473678894779589"))


def get_date(date_num: str) ->str:
    """Функция, которая меняет формат даты"""
    date = ""
    for i in date_num:
        if i.isalpha():
            break
        date += i

    return date[-2:] + "." + date[5:7] + "." + date[0:4]

if __name__ == "__main__":
    print(get_date("2024-03-11T02:26:18.671407"))

