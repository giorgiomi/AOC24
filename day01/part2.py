import numpy as np

# Load the data
data = np.loadtxt('input.txt', dtype=int)
data = np.sort(data, axis=0)

sum = 0
for i,x in enumerate(data[:,0]):
    start_idx = -1
    end_idx = -1
    for j,y in enumerate(data[:,1]):
        if start_idx == -1:
            if x == y: 
                start_idx = j
            continue
        end_idx = j
        if x!= y:
            break
    sum += x * (end_idx - start_idx)

print(sum)
