import numpy as np
from copy import copy, deepcopy

def findGuard(data):
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            if b == '^':
                return i,j

with open('input.txt', 'r') as f:
    data = [[el for el in line if el != '\n'] for line in f]
    map = deepcopy(data)
    # print(np.matrix(map))

    # initial position and direction
    i_start, j_start = findGuard(data)
    data[i_start][j_start] = 'N'
    dir = 'N'
    i, j = i_start, j_start

    # directions list
    directions = ['N', 'E', 'S', 'W']

    count = 0
    for k in range(len(map)):
        for l in range(len(map[k])):
            if map[k][l] == '.':
                data = deepcopy(map)
                data[i_start][j_start] = 'N'
                dir = 'N'
                i, j = i_start, j_start

                print(f"inserting # in {k, l}")
                data[k][l] = '#'
                # print(np.matrix(data))

                # solve labirinth
                while (True):
                    if dir == 'N':
                        if i == 0: break
                        else:
                            look = data[i-1][j]
                            if look == '.' or look in directions:
                                if look == dir:
                                    count += 1
                                    break
                                data[i-1][j] = 'N'
                                i -= 1
                            elif look == '#': dir = 'E'
                            
                    if dir == 'E':
                        if j == len(data[i]) - 1: break
                        else:
                            look = data[i][j+1]
                            if look == '.' or look in directions:
                                if look == dir:
                                    count += 1
                                    break
                                data[i][j+1] = 'E'
                                j += 1
                            elif look == '#': dir = 'S'
                            
                    if dir == 'S':
                        if i == len(data) - 1: break
                        else:
                            look = data[i+1][j]
                            if look == '.' or look in directions:
                                if look == dir:
                                    count += 1
                                    break
                                data[i+1][j] = 'S'
                                i += 1
                            elif look == '#': dir = 'W'
                            
                    if dir == 'W':
                        if j == 0: break
                        else:
                            look = data[i][j-1]
                            if look == '.' or look in directions:
                                if look == dir:
                                    count += 1
                                    break
                                data[i][j-1] = 'W'
                                j -= 1
                            elif look == '#': dir = 'N'

                # print(np.matrix(data))
                # data[k][l] = '.'
                

print(count)
