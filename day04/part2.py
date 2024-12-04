import numpy as np

data = np.loadtxt('input.txt', dtype=str)

count = 0
for i in range(1, len(data) - 1):
    for j in range(1, len(data[i]) - 1):
        if (data[i][j] == 'A'):
            if (data[i+1][j+1] == 'S' and data[i-1][j-1] == 'M'):
                if (data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S'):
                    count += 1
                if (data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M'):
                    count += 1
            if (data[i+1][j+1] == 'M' and data[i-1][j-1] == 'S'):
                if (data[i+1][j-1] == 'M' and data[i-1][j+1] == 'S'):
                    count += 1
                if (data[i+1][j-1] == 'S' and data[i-1][j+1] == 'M'):
                    count += 1

print(count)