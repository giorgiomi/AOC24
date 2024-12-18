import numpy as np
import sys

if sys.argv[1] == 'input':
    width = 101
    height = 103
elif sys.argv[1] == 'test':
    width = 11
    height = 7
else:
    print("Wrong parameter")
    exit()
n_steps = 100

def countRobots(r):
    count = [0, 0, 0, 0]
    for i in range(0, len(r), 2):
        x = r[i]
        y = r[i+1]
        if x < (width - 1)/2 and y < (height - 1)/2:
            count[0] += 1
        elif x > (width - 1)/2 and y < (height - 1)/2:
            count[1] += 1
        elif x > (width - 1)/2 and y > (height - 1)/2:
            count[2] += 1
        elif x < (width - 1)/2 and y > (height - 1)/2:
            count[3] += 1
    return count[0] * count[1] * count[2] * count[3]

r = []
v = []
with open(f'{sys.argv[1]}.txt', 'r') as f:
    data = f.readlines()
    for el in data:
        px, py = el.split(' ')[0].split('=')[1].split(',')
        px = int(px)
        py = int(py)
        vx, vy = el.split(' ')[1].split('=')[1].split(',')
        vx = int(vx)
        vy = int(vy)
        # print(px, py, vx, vy)
        r.extend((px, py))
        v.extend((vx, vy))
    # print(r, v)
# print(r)

for i in range(n_steps):
    for j in range(len(r)):
        r[j] += v[j]
        if j % 2 == 0: #x
            if r[j] >= width:
                r[j] -= width
            elif r[j] < 0:
                r[j] += width
        else: #y
            if r[j] >= height:
                r[j] -= height
            elif r[j] < 0:
                r[j] += height
# print(r)
count = countRobots(r)
print(count)
