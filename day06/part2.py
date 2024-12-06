import numpy as np

def findGuard(data):
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            if b == '^':
                return i,j

with open('test.txt', 'r') as f:
    data = [[el for el in line if el != '\n'] for line in f]

    # initial position and direction
    i, j = findGuard(data)
    data[i][j] = 'N'
    dir = 'N'

    # directions list
    directions = ['N', 'E', 'S', 'W']

    count = 0
    while (True):
        # update guard
        if dir == 'N':
            if i == 0:
                break
            elif data[i-1][j] == '.':
                data[i-1][j] = 'N'
                i -= 1
            elif data[i-1][j] in directions:
                # if data[i-1][j] == 'E':
                #     data_print = data
                #     data_print[i-2][j] = 'O'
                #     # print(np.matrix(data_print))
                #     count += 1
                data[i-1][j] = 'N'
                i -= 1
            elif data[i-1][j] == '#':
                dir = 'E'

            # scanning E
            for j_scan in range(j + 1, len(data[i])):
                if data[i][j_scan] == '#':
                    # scanning S
                    for i_scan in range(i, -1, -1):
                        if data[i_scan][j_scan - 1] == '#':
                            break
                        if data[i_scan][j_scan - 1] == 'S':
                            data_print = data
                            # data_print[i-1][j] = 'O'
                            # print(np.matrix(data_print))
                            count += 1
                            break
                    break
                if data[i][j_scan] == 'E':
                    data_print = data
                    # data_print[i-1][j] = 'O'
                    # print(np.matrix(data_print))
                    count += 1
                    break

        if dir == 'E':
            if j == len(data[i]) - 1:
                break
            elif data[i][j+1] == '.':
                data[i][j+1] = 'E'
                j += 1
            elif data[i][j+1] in directions:
                # if data[i][j+1] == 'S':
                #     data_print = data
                #     data_print[i][j+2] = 'O'
                #     # print(np.matrix(data_print))
                #     count += 1
                data[i][j+1] = 'E'
                j += 1
            elif data[i][j+1] == '#':
                dir = 'S'
            
            # scanning S
            for i_scan in range(i + 1, len(data)):
                if data[i_scan][j] == '#':
                    # scanning W
                    for j_scan in range(j, -1, -1):
                        if data[i_scan - 1][j_scan] == '#':
                            break
                        if data[i_scan - 1][j_scan] == 'W':
                            data_print = data
                            # data_print[i][j+1] = 'O'
                            # print(np.matrix(data_print))
                            count += 1
                            break
                    break
                if data[i_scan][j] == 'S':
                    data_print = data
                    # data_print[i][j+1] = 'O'
                    # print(np.matrix(data_print))
                    count += 1
                    break

        if dir == 'S':
            if i == len(data) - 1:
                break
            elif data[i+1][j] == '.':
                data[i+1][j] = 'S'
                i += 1
            elif data[i+1][j] in directions:
                # if data[i+1][j] == 'W':
                #     data_print = data
                #     data_print[i+2][j] = 'O'
                #     # print(np.matrix(data_print))
                #     count += 1
                data[i+1][j] = 'S'
                i += 1
            elif data[i+1][j] == '#':
                dir = 'W'
            
            # scanning W
            for j_scan in range(j - 1, -1, -1):
                if data[i][j_scan] == '#':
                    # scanning N
                    for i_scan in range(i, -1, -1):
                        if data[i_scan][j_scan + 1] == '#':
                            break
                        if data[i_scan][j_scan + 1] == 'N':
                            data_print = data
                            # data_print[i+1][j] = 'O'
                            # print(np.matrix(data_print))
                            count += 1
                            break
                    break
                if data[i][j_scan] == 'W':
                    data_print = data
                    # data_print[i+1][j] = 'O'
                    # print(np.matrix(data_print))
                    count += 1
                    break
                

        if dir == 'W':
            if j == 0:
                break
            elif data[i][j-1] == '.':
                data[i][j-1] = 'W'
                j -= 1
            elif data[i][j-1] in directions:
                # if data[i][j-1] == 'N':
                #     data_print = data
                #     data_print[i][j-2] = 'O'
                #     # print(np.matrix(data_print))
                #     count += 1
                data[i][j-1] = 'W'
                j -= 1
            elif data[i][j-1] == '#':
                dir = 'N'
            
            # scanning N
            for i_scan in range(i - 1, -1, -1):
                print(i_scan)
                if data[i_scan][j] == '#':
                    # scanning E
                    for j_scan in range(j, len(data[i_scan]) - 1):
                        if data[i_scan + 1][j_scan] == '#':
                            break
                        if data[i_scan + 1][j_scan] == 'E':
                            data_print = data
                            # data_print[i][j-1] = 'O'
                            # print(np.matrix(data_print))
                            count += 1
                            break
                    break
                if data[i_scan][j] == 'N':
                    data_print = data
                    # data_print[i][j-1] = 'O'
                    # print(np.matrix(data_print))
                    count += 1
                    break


# print(np.matrix(data))
#np.savetxt('output.txt', np.matrix(data))
print(f"count = {count}")
