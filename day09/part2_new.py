import numpy as np
import sys

file = sys.argv[1]

with open(f'{file}.txt', 'r') as f:
    data = np.array([int(x) for x in f.read()])
    # print(data)

    ids = np.arange(int(len(data)/2) + 1)
    # print(ids)

    lengths = data[::2]
    dots = data[1::2]
    # print(lengths)
    # print(dots)
    files = np.array([(lengths[i], ids[i]) for i in range(len(lengths))])
    # print(list(files))
    # print(dots)

    for i in np.arange(len(files) - 1, -1, -1):
        # print(f"i = {i}")
        file_len = files[i][0]
        file_id = files[i][1]
        for j in np.arange(len(dots)):
            if j < i:
                # print(f"j = {j}")
                dot_len = dots[j]
                if dot_len >= file_len:
                    #swap
                    # print("swapping")
                    files = np.delete(files, i, axis=0)
                    files = np.insert(files, j+1, (file_len, file_id), axis=0)

                    dots = np.insert(dots, j, 0)
                    # print(dots)
                    dots[j + 1] -= file_len
                    # print(dots)
                    if i == len(files) - 1:
                        dots = np.delete(dots, -1)
                        # print(dots)
                    else:
                        dots[i] += dots[i+1] + file_len
                        dots = np.delete(dots, i+1)
                    
                    # print(f"f:{files}")
                    # print(f"d:{dots}")
                    break
    
    # print(f"f:{files}")
    # print(f"d:{dots}")

    pos = 0
    checksum = 0
    for i, f in enumerate(files):
        # print(f"i = {i} f = {f} pos = {pos}")
        for k in range(f[0]):
            checksum += f[1] * (pos + k)
        pos += f[0]
        # print(f"checksum = {checksum}")
        if i == len(files) - 1:
            break
        else:
            pos += dots[i]
    print(checksum)
    print(files[:20])
    print(dots[:20])
