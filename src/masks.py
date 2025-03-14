def get_mask_card_number() -> str:
    """Функция принимает номер карты и возвращает ее маску"""
    number = input("Ваш номер карты:")
    correct_number = number[0:7] + number[7:14] + number[14:19]
    number_mask = correct_number[0:4] + " " + correct_number[4:6] + "" + " " + "****" + " " + correct_number[12:16]
    return number_mask


def get_mask_account() -> str:
    """Функция принимает номер счета и возвращает его маску"""
    number = input("Номер вашего счета:")
    number_mask = "" + number[-4:]
    return number_mask
print(get_mask_card_number())
print(get_mask_account())