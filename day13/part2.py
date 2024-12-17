import numpy as np
import sys

n_max = 100
costA = 3
costB = 1
corr = 10000000000000

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, c):
        return self.__class__(c*self.x, c*self.y)
    __rmul__ = __mul__
    
    def __add__(self, other):
        return self.__class__(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vec({self.x}, {self.y})"

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

with open(f'{sys.argv[1]}.txt', 'r') as f:

    data = f.readlines()
    cost = 0
    for i in range(0, len(data), 4):
        strA = data[i]
        strB = data[i+1]
        strP = data[i+2]
        
        dAx = int(strA.split('+')[1].split(',')[0])
        dAy = int(strA.split(', ')[1].split('+')[1])
        A = Vector(dAx, dAy)

        dBx = int(strB.split('+')[1].split(',')[0])
        dBy = int(strB.split(', ')[1].split('+')[1])
        B = Vector(dBx, dBy)

        Px = int(strP.split('=')[1].split(',')[0]) + corr
        Py = int(strP.split('Y=')[1]) + corr
        P = Vector(Px, Py)
        # print(P)

        num1 = A.y * P.x - A.x * P.y
        num2 = - B.y * P.x + B.x * P.y
        den = B.x * A.y - B.y * A.x
        if num1 % den == 0 and num2 % den == 0:
            n = num1/den
            m = num2/den
            cost += 3 * m + n

    print(int(cost))        




        
        

