from math import factorial
from itertools import permutations
def Enumerator(number):
    print (factorial(number))

    number = list(permutations(range(1, number + 1)))
    for i in number:
        print(' '.join(map(str, i)))

Enumerator(3) 