import numpy as np

def findGuard(data):
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            if b == '^':
                return i,j

with open('input.txt', 'r') as f:
    data = [[el for el in line if el != '\n'] for line in f]

    # initial position and direction
    i, j = findGuard(data)
    data[i][j] = 'N'
    dir = 'N'

    # directions list
    directions = ['N', 'E', 'S', 'W']

    count = 0
    while (True):

        if dir == 'N':
            if i == 0: break
            else:
                look = data[i-1][j]
                if look == '.' or look in directions:
                    # if look == 'E':
                    #     count += 1
                    #     print(np.matrix(data))
                    # else:
                    for j_scan in range(j + 1, len(data[i])):
                        if data[i][j_scan] == '#': break
                        if data[i][j_scan] == 'E':
                            count += 1
                            # print(np.matrix(data))
                            break
                    data[i-1][j] = 'N'
                    i -= 1
                elif look == '#': dir = 'E'
                

        if dir == 'E':
            if j == len(data[i]) - 1: break
            else:
                look = data[i][j+1]
                if look == '.' or look in directions:
                    # if look == 'S':
                    #     count += 1
                    #     print(np.matrix(data))
                    # else:
                    for i_scan in range(i + 1, len(data)):
                        if data[i_scan][j] == '#': break
                        if data[i_scan][j] == 'S':
                            count += 1
                            # print(np.matrix(data))
                            break
                    data[i][j+1] = 'E'
                    j += 1
                elif look == '#': dir = 'S'
                

        if dir == 'S':
            if i == len(data) - 1: break
            else:
                look = data[i+1][j]
                if look == '.' or look in directions:
                    # if look == 'W':
                    #     count += 1
                    #     print(np.matrix(data))
                    # else:
                    for j_scan in range(j - 1, -1, -1):
                        if data[i][j_scan] == '#': break
                        if data[i][j_scan] == 'W':
                            count += 1
                            # print(np.matrix(data))
                            break
                    data[i+1][j] = 'S'
                    i += 1
                elif look == '#': dir = 'W'
                

        if dir == 'W':
            if j == 0: break
            else:
                look = data[i][j-1]
                if look == '.' or look in directions:
                    # if look == 'N':
                    #     count += 1
                    #     print(np.matrix(data))
                    # else:
                    for i_scan in range(i - 1, -1, -1):
                        if data[i_scan][j] == '#': break
                        if data[i_scan][j] == 'N':
                            count += 1
                            # print(np.matrix(data))
                            break
                    data[i][j-1] = 'W'
                    j -= 1
                elif look == '#': dir = 'N'
                

#print(np.matrix(data))
print(count)

#print(list(range(5, -1, -1)))