def get_mask_card_number(number: int) -> str:
    """Функция принимает номер карты и возвращает ее маску"""
    number = str(number)
    correct_number = number[0:7] + number[7:14] + number[14:19]
    if not correct_number.isdigit() or len(correct_number) != 16:
        return 'Error'
    number_mask = correct_number[0:4] + " " + correct_number[4:6] + "**" + " " + "****" + " " + correct_number[12:16]
    return number_mask


def get_mask_account(number: int) -> str:
    """Функция принимает номер счета и возвращает его маску"""
    number = str(number)
    if len(number) != 20 or not number.isdigit():
        return "Error"
    number_mask = "**" + number[-4:]
    return number_mask
