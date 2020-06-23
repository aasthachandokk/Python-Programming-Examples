import math

def permutation_combination(objects, time):
    p = math.factorial(objects) / math.factorial(objects - time)
    c = p / time
    print('Permutations of {} objects take at {} time : {:.0f}'.format(objects, time, p))
    print('Combinations of {} objects take at {} time : {:.0f}'.format(objects, time, c))

permutation_combination(5, 2)
