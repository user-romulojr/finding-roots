precision_error = 14

def fix_error(num):
    negative = num < 0
    if negative:
        num *= -1

    base10 = 10 ** (precision_error+1)
    num = int(num * base10)
    if num % 10 >= 5:
        num += 10
    num = num // 10
    num /= base10 / 10

    if negative:
        num *= -1
    return num

def my_round(num, places):
    negative = num < 0
    if negative:
        num *= -1

    num = fix_error(num)

    base10 = 10 ** (places+1)
    num = int(num * base10)
    if num % 10 >= 5:
        num += 10
    num = num // 10
    num /= base10 / 10

    if negative:
        num *= -1
    return num


def sign(x0, x1):
    return (x0 < 0 and x1 < 0) or (x0 > 0 and x1 > 0)

def get_error(cur, prv):
    absolute_error = abs(cur-prv)
    ans = abs(absolute_error/cur) * 100
    return ans