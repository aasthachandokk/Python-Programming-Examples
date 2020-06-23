l = [1,2,3,4,5,6,7,8,9]

def isodd(x):
    if x%2 != 0:
        return True
    else:
        return False
    
list(filter(isodd,l))

# Alternative method-
#list(filter(lambda x: x%2 != 0, l))
