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

def move(dA, dB, P):
    max_cost = n_max * costA + n_max * costB
    min_cost = max_cost
    for i in range(n_max):
        for j in range(n_max):
            res = dA * i + dB * j
            if res == P:
                cost = i * costA + j * costB
                if cost < min_cost:
                    min_cost = cost
    if min_cost == max_cost:
        return 0
    else:
        return min_cost

with open(f'{sys.argv[1]}.txt', 'r') as f:

    data = f.readlines()
    cost = 0
    for i in range(0, len(data), 4):
        strA = data[i]
        strB = data[i+1]
        strP = data[i+2]
        
        dAx = int(strA.split('+')[1].split(',')[0])
        dAy = int(strA.split(', ')[1].split('+')[1])
        dA = Vector(dAx, dAy)

        dBx = int(strB.split('+')[1].split(',')[0])
        dBy = int(strB.split(', ')[1].split('+')[1])
        dB = Vector(dBx, dBy)

        Px = int(strP.split('=')[1].split(',')[0]) + corr
        Py = int(strP.split('Y=')[1]) + corr
        P = Vector(Px, Py)
        print(P)

        curr_cost = move(dA, dB, P)
        # # print(curr_cost)
        cost += curr_cost
        
    print(cost)        




        
        

