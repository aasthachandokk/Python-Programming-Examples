def cubesum(num):
    result = 0
    while (num != 0):
        result += ((num % 10)**3) 
        num //= 10      
    return result

def isArmstrong(num):
    if cubesum(num) == num:
        return True
    else:
        return False

def PrintArmstrong(num):
    if isArmstrong(num) == True:
        return num
    else:
        pass

cubesum(153)
isArmstrong(153)
PrintArmstrong(153)
