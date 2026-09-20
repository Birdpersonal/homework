def get_mask_card_number(nums: int) -> str:
    """Принимает номер карты и возвращает маску"""

    str_nums = str(nums)
    mask_card_number = str_nums[0:4] + " " + str_nums[4:6] + "**" + " " + "****" + " " + str_nums[-4:]
    return mask_card_number


def get_mask_account(nums: int) -> str:
    """Принимает номер счета и возвращает маску"""
    str_nums = str(nums)
    mask_account = "**" + str_nums[-4:]
    return mask_account


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
