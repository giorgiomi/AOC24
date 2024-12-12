import numpy as np

def numberDigits(n):
    return int(np.floor(np.log10(float(n)))) + 1

def splitNumber(n):
    n_str = str(n)
    return (int(n_str[:int(len(n_str)/2)]), int(n_str[int(len(n_str)/2):]))

def blink(arr):
    i = 0
    while (i < len(arr)):
        if arr[i] == 0:
            arr[i] = 1
        elif numberDigits(arr[i]) % 2 == 0:
            arr = np.insert(arr, i, splitNumber(arr[i]))
            arr = np.delete(arr, i + 2)
            i += 1
        else:
            arr[i] *= 2024
        i += 1
    return arr

data = np.loadtxt('input.txt', dtype=int)
N = 25
for i in range(N):
    print(i)
    data = blink(data)
print(len(data))
