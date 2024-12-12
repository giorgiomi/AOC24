import numpy as np

# data = np.loadtxt('input.txt', dtype=int, delimiter='')
with open('input.txt', 'r') as f:
    data = [[int(el) for el in line if el != '\n'] for line in f]
    # data = np.matrix(data)

# print(data)

def lookAround(i, j, score, locations):
    val = data[i][j]
    if val == 9:
        # print(f"9 found at {i, j}")
        if (i, j) not in locations:
            score += 1
            locations.add((i, j))
        return score
    else:
        next = val + 1

        if i >= 1 and next == data[i-1][j]:
            # print("N")
            score = lookAround(i-1, j, score, locations) #N
        if j <= len(data[i]) - 2 and next == data[i][j+1]:
            # print("E")
            score = lookAround(i, j+1, score, locations) #E
        if i <= len(data) - 2 and next == data[i+1][j]:
            # print("S")
            score = lookAround(i+1, j, score, locations) #S
        if j >= 1 and next == data[i][j-1]:
            # print("W")
            score = lookAround(i, j-1, score, locations) #W
        return score
    
    

sum = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if data[i][j] == 0:
            # print(f"0 found at {i, j}")
            # it's a trailhead, we have to count the score
            locations = set()
            sum += lookAround(i, j, 0, locations)
print(sum)