import numpy as np

def swap(i, j, arr):
    t = arr[i]
    arr[i] = arr[j]
    arr[j] = t
    return arr

def findLast(arr):
    for i, el in reversed(list(enumerate(arr))):
        if el != -1:
            return i

def findFirst(arr):
    for i, el in enumerate(arr):
        if el == -1:
            return i

data = str(np.loadtxt('test.txt', dtype=str))
blocks = []
id = 0
for i, c in enumerate(data):
    if i % 2 == 0:
        blocks.extend([id]*int(c))
        id += 1
    else:
        blocks.extend([-1]*int(c))

#print(len(blocks))
blocks = np.array(blocks)
print(blocks)
#exit()

file_length = 0
val = blocks[-1]
#for i, el in reversed(list(enumerate(blocks))):
for i in np.arange(len(blocks) - 1, -1, -1):
    print(i)
    if blocks[i] == -1:
        continue
    else:
        if blocks[i] == blocks[i - 1]:
            file_length += 1
            continue
        else:
            file_length += 1
            # insert cycle here
            for l in np.arange(len(blocks)):
                i_first = l + findFirst(blocks[l:])
                dot_length = 0
                for j, el2 in list(enumerate(blocks))[i_first:]:
                    if el2 == -1:
                        dot_length += 1
                    else:
                        break
                # print(f"dots: {dot_length}")
                # print(f"file: {file_length}")
                if dot_length >= file_length and i > i_first:
                    # do the swap
                    #print(f"swapping file of {file_length} in {dot_length} dots")
                    for k in range(file_length):
                        blocks = swap(i + k, i_first + k, blocks)
                        #print("swapping")
                    #print(blocks)
                    break
                else:
                    # move to next dots
                    continue
            file_length = 0
    
print(blocks)

checksum = 0
for i, el in enumerate(blocks):
    if el != -1:
        checksum += el*i
print(checksum)