def MDR(num):
    string = str(num)
    while len(string) > 1:
        string = str(prodDigits(int(string)))
    return int(string)
    
def MPersistence(num):
    string = str(num)
    persistence = 0
    while len(string) > 1:
        string = str(prodDigits(int(string)))
        persistence += 1
    return persistence

print(MDR(86))
print(MPersistence(86))
