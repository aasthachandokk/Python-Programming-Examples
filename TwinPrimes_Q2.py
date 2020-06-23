def is_prime(num):            #function to check if number is prime or not
    for i in range(2,num):
        if (num % i) == 0:    #number greater than 1 that is not a product of two natural numbers is prime number
            return False
    return True

print('Twin prime numbers less than 1000 are:')
for num1 in range(0,1000):     #printing twin primes less than 1000
    num2 = num1 + 2
    if num1%2 != 0 and num2%2 != 0:       #checking if the number is odd number or not
        if (is_prime(num1) and is_prime(num2)):
            print('({},{})'.format(num1,num2))
