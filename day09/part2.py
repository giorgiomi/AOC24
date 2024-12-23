import numpy as np
import sys

file = sys.argv[1]

with open(f'{file}.txt', 'r') as f:
    data = np.array([int(x) for x in f.read()])

    ids = np.arange(int(len(data)/2) + 1)

    lengths = data[::2]
    dots = data[1::2]
    files = np.array([(lengths[i], ids[i]) for i in range(len(lengths))])

    i = len(files) - 1
    while (i >= 0):
        file_len = files[i][0]
        file_id = files[i][1]
        for j in np.arange(len(dots)):
            if j < i:
                dot_len = dots[j]
                if dot_len >= file_len:
                    #swap
                    files = np.delete(files, i, axis=0)
                    files = np.insert(files, j+1, (file_len, file_id), axis=0)

                    dots = np.insert(dots, j, 0)
                    dots[j + 1] -= file_len
                    if i == len(files) - 1:
                        dots = np.delete(dots, -1)
                    else:
                        dots[i] += dots[i+1] + file_len
                        dots = np.delete(dots, i+1)
                    
                    i += 1
                    break
        i -= 1

    pos = 0
    checksum = 0
    for i, f in enumerate(files):
        for k in range(f[0]):
            checksum += f[1] * (pos + k)
        pos += f[0]
        if i == len(files) - 1:
            break
        else:
            pos += dots[i]
    print(checksum)
