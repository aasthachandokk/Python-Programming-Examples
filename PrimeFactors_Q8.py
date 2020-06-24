import math

def PrimeFactors(num):
    for i in range(2,int(math.sqrt(num)+1)):
        while (num%i) == 0:
            print(i)
            num = num/i
    if num > 2:
        print(int(num))
            
PrimeFactors(88)
