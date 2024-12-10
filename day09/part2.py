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

def findFirst(arr):
    for i, el in enumerate(arr):
        if el == '.':
            return i

data = str(np.loadtxt('test.txt', dtype=str))
blocks = []
id = 0
for i, c in enumerate(data):
    if i % 2 == 0:
        blocks.extend([id]*int(c))
        id += 1
    else:
        blocks.extend(['.']*int(c))
print(blocks)

#print(len(blocks))

file_length = 0
val = blocks[-1]
for i, el in reversed(list(enumerate(blocks))):
    if el == '.':
        continue
    else:
        if el == blocks[i - 1]:
            file_length += 1
            continue
        else:
            file_length += 1
            # insert cycle here(?)
            i_first = findFirst(blocks)
            dot_length = 0
            for j, el2 in list(enumerate(blocks))[i_first:]:
                if el2 == '.':
                    dot_length += 1
                else:
                    break
            print(f"dots: {dot_length}")
            print(f"file: {file_length}")
            if dot_length >= file_length:
                # do the swap
                for k in range(file_length):
                    blocks = swap(i + k, i_first + k, blocks)
                    print("swapping")
                print(blocks)
            file_length = 0
    
    
print(blocks)

checksum = 0
for i, el in enumerate(blocks):
    if el != '.':
        checksum += el*i
print(checksum)