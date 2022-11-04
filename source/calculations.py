LAST_SLAB_LITRE = 3000
LAST_SLAB_LITRE_COST = 8

def get_ratio_total(ratio):
    numbers = ratio.replace(':', ' ').split()
    ratio_total = 0
    for num in numbers:
        ratio_total += int(num)
    return ratio_total, numbers

def get_ratio_of_number(number, ratio):
    ratio_total, numbers = get_ratio_total(ratio)
    final_result = ''
    for num in numbers:
        calc = int(number) * (int(num) / int(ratio_total))
        final_result += str(calc) + ' '
    return final_result.split()

def income_tax_calculation(number, slab):
    total = 0
    for key, value in slab:
        if number - value >= 0:
            number -= value
            total += value * key
        elif number == 0:
            pass
        elif number - value < 0:
            total += number * key
            number = 0
    return total