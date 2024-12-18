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
        for j in range(len(map[i]) - 1):
            if map[i][j] == '[' and map[i][j+1] == ']':
                sum += 100 * i + j
    return sum

def enlargeMap(map):
    new_map = [[0 for i in range(2*len(map[0]))] for j in range(len(map))]
    for i in range(len(map)):
        for j in range(len(map[i])):
            tile = map[i][j]
            if tile == '#':
                new_map[i][2*j] = '#'
                new_map[i][2*j+1] = '#'
            elif tile == 'O':
                new_map[i][2*j] = '['
                new_map[i][2*j+1] = ']'
            elif tile == '.':
                new_map[i][2*j] = '.'
                new_map[i][2*j+1] = '.'
            elif tile == '@':
                new_map[i][2*j] = '@'
                new_map[i][2*j+1] = '.'
    return new_map

def lookBoxesUp(map, i, j, boxes):
    if map[i-1][j] == '[':
        boxes.add((i-1, j))
        boxes = lookBoxesUp(map, i-1, j, boxes)
        if len(boxes) == 0:
            return set()
        boxes = lookBoxesUp(map, i-1, j+1, boxes)
        if len(boxes) == 0:
            return set()
    if map[i-1][j] == ']':
        boxes.add((i-1, j-1))
        boxes = lookBoxesUp(map, i-1, j, boxes)
        if len(boxes) == 0:
            return set()
        boxes = lookBoxesUp(map, i-1, j-1, boxes)
        if len(boxes) == 0:
            return set()
    if map[i-1][j] == '#':
        return set()
    return boxes
    

def lookBoxesDown(map, i, j, boxes):
    if map[i+1][j] == '[':
        boxes.add((i+1, j))
        boxes = lookBoxesDown(map, i+1, j, boxes)
        if len(boxes) == 0:
            return set()
        boxes = lookBoxesDown(map, i+1, j+1, boxes)
        if len(boxes) == 0:
            return set()
    if map[i+1][j] == ']':
        boxes.add((i+1, j-1))
        boxes = lookBoxesDown(map, i+1, j, boxes)
        if len(boxes) == 0:
            return set()
        boxes = lookBoxesDown(map, i+1, j-1, boxes)
        if len(boxes) == 0:
            return set()
    if map[i+1][j] == '#':
        return set()
    return boxes


with open(f'{case}A.txt', 'r') as f:
    map = [[el for el in line if el != '\n'] for line in f]
    map = enlargeMap(map)

# printNice(map)

with open(f'{case}B.txt', 'r') as f:
    moves = []
    for line in f:
        for el in line:
            if el != '\n':
                moves.append(el)

i_start, j_start = findRobot(map)
i, j = findRobot(map)
# map[i_start][j_start] = '.'

for k, move in enumerate(moves):
    # print(k)
    # printNice(map)
    # print('')
    # print(f'move = {move}')
    if move == '^':
        if map[i-1][j] == '#':
            continue
        elif map[i-1][j] == '.':
            # print('moving up')
            map[i][j] = '.'
            map[i-1][j] = '@'
            i -= 1
            continue
        elif map[i-1][j] == '[' or map[i-1][j] == ']':
            boxes = set()
            boxes = list(lookBoxesUp(map, i, j, boxes))
            boxes.sort()
            # print(boxes)
            if len(boxes) == 0:
                continue
            else:
                for boxPos in boxes:
                    # print(boxPos)
                    i_box = boxPos[0]
                    j_box = boxPos[1]
                    map[i_box][j_box] = '.'
                    map[i_box][j_box+1] = '.'
                    map[i_box-1][j_box] = '['
                    map[i_box-1][j_box+1] = ']'
                map[i-1][j] = '@'
                map[i][j] = '.'
                i -= 1
        else:
            print(f'found {map[i-1][j]}')
            break

    elif move == '>':
        if map[i][j+1] == '#':
            continue
        elif map[i][j+1] == '.':
            map[i][j+1] = '@'
            map[i][j] = '.'
            j += 1
            continue
        elif map[i][j+1] == '[':
            for m in range(j+3, len(map[i]), 2):
                if map[i][m] == '[' or map[i][m] == ']':
                    continue
                elif map[i][m] == '#':
                    break
                elif map[i][m] == '.':
                    for n in range(m, j+1, -1):
                        map[i][n] = map[i][n-1]
                    map[i][j+1] = '@'
                    map[i][j] = '.'
                    j += 1
                    break
        else:
            print(f'found {map[i][j+1]}')
            break

    elif move == 'v':
        if map[i+1][j] == '#':
            continue
        elif map[i+1][j] == '.':
            # print('moving down')
            map[i+1][j] = '@'
            map[i][j] = '.'
            i += 1
            continue
        elif map[i+1][j] == '[' or map[i+1][j] == ']':
            boxes = set()
            boxes = list(lookBoxesDown(map, i, j, boxes))
            boxes.sort(reverse=True)
            # print(boxes)
            if len(boxes) == 0:
                continue
            else:
                for boxPos in boxes:
                    # print(boxPos)
                    i_box = boxPos[0]
                    j_box = boxPos[1]
                    map[i_box][j_box] = '.'
                    map[i_box][j_box+1] = '.'
                    map[i_box+1][j_box] = '['
                    map[i_box+1][j_box+1] = ']'
                map[i+1][j] = '@'
                map[i][j] = '.'
                i += 1
        else:
            print(f'found {map[i+1][j]}')
            break

    elif move == '<':
        if map[i][j-1] == '#':
            continue
        elif map[i][j-1] == '.':
            map[i][j-1] = '@'
            map[i][j] = '.'
            j -= 1
            continue
        elif map[i][j-1] == ']':
            for m in range(j-2, -1, -1):
                if map[i][m] == '[' or map[i][m] == ']':
                    continue
                elif map[i][m] == '#':
                    break
                elif map[i][m] == '.':
                    for n in range(m, j-1):
                        map[i][n] = map[i][n+1]
                    map[i][j-1] = '@'
                    map[i][j] = '.'
                    j -= 1
                    break
        else:
            print(f'found {map[i][j-1]}')
            break
    

# printNice(map)
print(sumCoord(map))