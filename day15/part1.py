import sys
case = sys.argv[1]

def findRobot(data):
    for i, a in enumerate(data):
        for j, b in enumerate(a):
            if b == '@':
                return i, j

def printNice(map):
    for i in range(len(map)):
        for j in range(len(map[i])):
            print(map[i][j], end='', sep='')
        print('')

def sumCoord(map):
    sum = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                sum += 100 * i + j
    return sum

with open(f'{case}A.txt', 'r') as f:
    map = [[el for el in line if el != '\n'] for line in f]

with open(f'{case}B.txt', 'r') as f:
    moves = []
    for line in f:
        for el in line:
            if el != '\n':
                moves.append(el)

i_start, j_start = findRobot(map)
i, j = findRobot(map)
map[i_start][j_start] = '.'

for k, move in enumerate(moves):
    # print(f'move = {move}')
    if move == '^':
        if map[i-1][j] == '#':
            continue
        elif map[i-1][j] == '.':
            i -= 1
            continue
        elif map[i-1][j] == 'O':
            for m in range(i-2, -1, -1):
                if map[m][j] == 'O':
                    continue
                elif map[m][j] == '#':
                    break
                elif map[m][j] == '.':
                    map[m][j] = 'O'
                    map[i-1][j] = '.'
                    i -= 1
                    break
        else:
            print(f'found {map[i-1][j]}')
            break

    if move == '>':
        if map[i][j+1] == '#':
            continue
        elif map[i][j+1] == '.':
            j += 1
            continue
        elif map[i][j+1] == 'O':
            for m in range(j+2, len(map[i])):
                if map[i][m] == 'O':
                    continue
                elif map[i][m] == '#':
                    break
                elif map[i][m] == '.':
                    map[i][m] = 'O'
                    map[i][j+1] = '.'
                    j += 1
                    break
        else:
            print(f'found {map[i][j+1]}')
            break

    if move == 'v':
        if map[i+1][j] == '#':
            continue
        elif map[i+1][j] == '.':
            i += 1
            continue
        elif map[i+1][j] == 'O':
            for m in range(i+2, len(map)):
                if map[m][j] == 'O':
                    continue
                elif map[m][j] == '#':
                    break
                elif map[m][j] == '.':
                    map[m][j] = 'O'
                    map[i+1][j] = '.'
                    i += 1
                    break
        else:
            print(f'found {map[i+1][j]}')
            break

    if move == '<':
        if map[i][j-1] == '#':
            continue
        elif map[i][j-1] == '.':
            j -= 1
            continue
        elif map[i][j-1] == 'O':
            for m in range(j-2, -1, -1):
                if map[i][m] == 'O':
                    continue
                elif map[i][m] == '#':
                    break
                elif map[i][m] == '.':
                    map[i][m] = 'O'
                    map[i][j-1] = '.'
                    j -= 1
                    break
        else:
            print(f'found {map[i][j-1]}')
            break
    
    # printNice(map)
    # print('')

# printNice(map)
print(sumCoord(map))