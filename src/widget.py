def mask_account_card(number: str) -> str:
    """Функция принимает на вход номер карты или счета и возвращает их маску"""
    card_number = ""
    name_card = ""
    if "Счет" in number:
        score_number = number[5:]
        number_mask = number[0:4] + " " + "**" + score_number[-4:]
        return number_mask
    else:
        for i in range(len(number)):
            if number[i].isalpha() or number[i] == " ":
                name_card += number[i]
            else:
                card_number += number[i]

        correct_number = card_number[0:7] + card_number[7:14] + card_number[12:]
        number_mask = (
            name_card
            + ""
            + correct_number[0:4]
            + " "
            + correct_number[4:6]
            + "**"
            + " "
            + "****"
            + " "
            + correct_number[14:]
        )

        return number_mask

print(mask_account_card('Maestro 159683786prtyipt'))

def get_date(date: str) -> str:
    '''Функция принимает строку с датой в формате "2024-03-11T02:26:18.671407" и возвращает в формате "ДД.ММ.ГГГГ"'''
    return date[8:10] + "." + date[5:7] + "." + date[0:4]


