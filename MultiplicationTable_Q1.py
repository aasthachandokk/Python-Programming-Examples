def multiplication_table(number):
    n = 1
    while n <= 10:  #printing multiplication table till 10
        result = number * n
        print(number, '*' , n , '=' , result)
        n = n + 1
        
multiplication_table(2)
