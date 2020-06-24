def sumPdivisors(num):
    divisors = [1]
    for i in range(2, num):
        if (num % i) == 0:
            divisors.append(i)
    return sum(divisors)    
    
def perfectNum(lower, upper):
    num = []
    for i in range(lower,upper):
        if sumPdivisors(i) == i:
            num.append(i)
    return num
        
perfectNum(4,500)
