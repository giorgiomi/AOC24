import numpy as np

data = np.loadtxt('input.txt', dtype=str)

count = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if (data[i][j] == 'X'):
            # look in all 8 directions for 'MAS'
            # N
            if (i >= 3 and data[i-1][j] == 'M' and data[i-2][j] == 'A' and data[i-3][j] == 'S'):
                count += 1
            # E
            if (j < len(data[i]) - 3 and data[i][j+1] == 'M' and data[i][j+2] == 'A' and data[i][j+3] == 'S'):
                count += 1
            # S
            if (i < len(data) - 3 and data[i+1][j] == 'M' and data[i+2][j] == 'A' and data[i+3][j] == 'S'):
                count += 1
            # W
            if (j >= 3 and data[i][j-1] == 'M' and data[i][j-2] == 'A' and data[i][j-3] == 'S'):
                count += 1
            # NE
            if (i >= 3 and j < len(data[i]) - 3 and data[i-1][j+1] == 'M' and data[i-2][j+2] == 'A' and data[i-3][j+3] == 'S'):
                count += 1
            # SE
            if (i < len(data) - 3 and j < len(data[i]) - 3 and data[i+1][j+1] == 'M' and data[i+2][j+2] == 'A' and data[i+3][j+3] == 'S'):
                count += 1
            # NW
            if (i >= 3 and j >= 3 and data[i-1][j-1] == 'M' and data[i-2][j-2] == 'A' and data[i-3][j-3] == 'S'):
                count += 1
            # SW
            if (i < len(data) - 3 and j >= 3 and data[i+1][j-1] == 'M' and data[i+2][j-2] == 'A' and data[i+3][j-3] == 'S'):
                count += 1

print(count)