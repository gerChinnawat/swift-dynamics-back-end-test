def thousands_digit_to_roman(number_value: int):
    return number_value * 'M'

def hundreds_digit_to_roman(number_value: int):
    if number_value <= 3:
        return number_value * 'C'
    elif number_value == 4:
        return 'CD'
    elif number_value == 5:
        return 'D'
    elif number_value > 5 and number_value < 9:
        return 'D' + 'C' * (number_value -5)
    elif number_value == 9:
        return 'CM'

def tens_digit_to_roman(number_value: int):
    if number_value <= 3:
        return number_value * 'X'
    elif number_value == 4:
        return 'XL'
    elif number_value == 5:
        return 'L'
    elif number_value > 5 and number_value < 9:
        return 'L' + 'X' * (number_value - 5)
    elif number_value == 9:
        return 'XC'

def ones_digit_to_roman(number_value: int):
    if number_value <= 3:
        return number_value * 'I'
    elif number_value == 4:
        return 'IV'
    elif number_value == 5:
        return 'V'
    elif number_value > 5 and number_value < 9:
        return 'V' + 'I' * (number_value - 5)
    elif number_value == 9:
        return 'IX'