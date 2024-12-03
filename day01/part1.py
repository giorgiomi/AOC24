import numpy as np

# Load the data
data = np.loadtxt('input.txt', dtype=int)
data = np.sort(data, axis=0)
diff = np.abs(data[:,0] - data[:,1])
print(diff)
res = np.sum(diff)
print(res)