def get_mask_card_number(nums: int) -> str:
    """Принимает номер карты и возвращает маску"""
    str_nums = str(nums)
    if len(str_nums) == 0:
        return "Введите число"
    if not str_nums.isdigit():
        return "Введите номер карты без букв"
    if len(str_nums) != 16:
        return "Неккоректное количество цифр"
    mask_card_number = str_nums[0:4] + " " + str_nums[4:6] + "**" + " " + "****" + " " + str_nums[-4:]
    return mask_card_number


def get_mask_account(nums: int) -> str:
    """Принимает номер счета и возвращает маску"""
    str_nums = str(nums)
    if len(str_nums) == 0:
        return "Введите число"
    if not str_nums.isdigit():
        return "Введите номер карты без букв"
    if len(str_nums) != 20:
        return "Неккоректное количество цифр"
    mask_account = "**" + str_nums[-4:]
    return mask_account


