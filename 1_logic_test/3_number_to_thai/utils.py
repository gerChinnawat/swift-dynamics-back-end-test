def digit_number_to_th(number: int, digit_no: int, digit_total: int) -> str:
    match number:
        case 0:
            return 'ศูนย์' if digit_total == 1 and digit_no == 1 else ''
        case 1:
            if digit_total > 1 and digit_no == 1:
                return 'เอ็ด'
            elif digit_total > 1 and digit_no == 2:
                return 'สิบ'
            elif digit_total > 1 and digit_no == 8:
                return ''
            return 'หนึ่ง'
        case 2:
            return 'ยี่' if digit_total > 1 and digit_no == 2 else 'สอง'
        case 3:
            return 'สาม'
        case 4:
            return 'สี่'
        case 5:
            return 'ห้า'
        case 6:
            return 'หก'
        case 7:
            return 'เจ็ด'
        case 8:
            return 'แปด'
        case 9:
            return 'เก้า'
        case _:
            return ''

def digit_value_to_th(digit_no: int) -> str:    
    match digit_no:
        case 2:
            return 'สิบ'
        case 3:
            return 'ร้อย'
        case 4:
            return 'พัน'
        case 5:
            return 'หมื่น'
        case 6:
            return 'แสน'
        case 7:
            return 'ล้าน'
        case 8:
            return 'สิบล้าน'
        case _:
            return ''
