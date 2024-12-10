import numpy as np

def swap(i, j, arr):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr

def findLast(arr):
    for i, el in reversed(list(enumerate(arr))):
        if el != '.':
            return i

data = str(np.loadtxt('input.txt', dtype=str))
blocks = []
id = 0
for i, c in enumerate(data):
    if i % 2 == 0:
        blocks.extend([id]*int(c))
        id += 1
    else:
        blocks.extend(['.']*int(c))
#print(blocks)

print(len(blocks))

for i, el in enumerate(blocks):
    print(i)
    if el == '.':
        # swap with last element that's not a point
        j = findLast(blocks)
        if j <= i:
           break
        blocks = swap(i, j, blocks) 
#print(blocks)

checksum = 0
for i, el in enumerate(blocks):
    if el != '.':
        checksum += el*i
print(checksum)