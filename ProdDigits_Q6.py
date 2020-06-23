def prodDigits(num):
    product = 1
    while (num != 0):
        product *= (num % 10)
        num //= 10
    return product

prodDigits(345)
