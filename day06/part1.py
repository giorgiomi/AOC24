def findGuard(data):
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            if b == '^':
                return i,j

with open('input.txt', 'r') as f:
    data = [[el for el in line if el != '\n'] for line in f]

    # initial position and direction
    i, j = findGuard(data)
    data[i][j] = '.'
    dir = 'N'

    count = 0
    stop_count = 100
    while (True):
        # if (i, j) == (79, 88) or count == stop_count:
        #     break
        # print(i, j, dir)
        # update guard
        if dir == 'N':
            if i == 0:
                if data[i][j] != 'X':
                    count += 1
                break
            elif data[i-1][j] == '.':
                #move N
                count += 1
                data[i-1][j] = 'X'
                i -= 1
            elif data[i-1][j] == 'X':
                #move N
                i -= 1
            elif data[i-1][j] == '#':
                #turn E
                dir = 'E'

        if dir == 'E':
            if j == len(data[i]) - 1:
                if data[i][j] != 'X':
                    count += 1
                break
            elif data[i][j+1] == '.':
                #move E
                count += 1
                data[i][j+1] = 'X'
                j += 1
            elif data[i][j+1] == 'X':
                #move N
                j += 1
            elif data[i][j+1] == '#':
                #turn S
                dir = 'S'

        if dir == 'S':
            if i == len(data) - 1:
                if data[i][j] != 'X':
                    count += 1
                break
            elif data[i+1][j] == '.':
                #move S
                count += 1
                data[i+1][j] = 'X'
                i += 1
            elif data[i+1][j] == 'X':
                #move S
                i += 1
            elif data[i+1][j] == '#':
                #turn E
                dir = 'W'

        if dir == 'W':
            if j == 0:
                if data[i][j] != 'X':
                    count += 1
                break
            elif data[i][j-1] == '.':
                #move W
                count += 1
                data[i][j-1] = 'X'
                j -= 1
            elif data[i][j-1] == 'X':
                #move W
                j -= 1
            elif data[i][j-1] == '#':
                #turn S
                dir = 'N'


print(count)
