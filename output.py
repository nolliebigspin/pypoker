def transform(number):
    value = ""
    if number == 1:
        value = "Ace"
    elif number == 11:
        value = "Jack"
    elif number == 12:
        value = "Queen"
    elif number == 13:
        value == "King"
    else:
        value = str(number)
    return value

def out_single_card(card):
    print("{}, {}".format(card.color.capitalize(), transform(card.number)))
