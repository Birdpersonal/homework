from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(num_namber: str) -> str:
    """Функция обрабатывает информацию о счетах и картах"""
    letter = num_namber.split()
    nums = letter[-1]
    name = " ".join(letter[:-1])
    if name not in ["Visa Platinum", "Visa Classic", "Visa Platinum", "Visa Gold", "MasterCard", "Maestro", "Счет"]:
        return "Такой карты нет"
    if name in ["Visa Platinum", "Visa Classic", "Visa Platinum", "Visa Gold" "MasterCard", "Maestro"]:
        if len(nums) != 16:
            return "Неточное количество цифр"
        result = get_mask_card_number(int(nums))
    elif name == "Счет":
        if len(nums) != 20:
            return "Неточное количество цифр"
        result = get_mask_account(int(nums))
    else:
        result = ""

    return f"{name} {result}"


if __name__ == "__main__":
    print(mask_account_card("Visa Classic 68319824767658"))


def get_date(date_num: str) -> str:
    """Функция, которая меняет формат даты"""
    if not date_num:
        return "Введите дату"
    date = ""
    for i in date_num:
        if i.isalpha():
            break
        date += i

    return date[-2:] + "." + date[5:7] + "." + date[0:4]


if __name__ == "__main__":
    print(get_date(""))
