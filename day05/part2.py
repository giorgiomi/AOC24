import numpy as np
import sys

def swap(i, j, arr):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

rules = np.loadtxt(f'{sys.argv[1]}A.txt', delimiter='|', dtype=int)
rules = rules[rules[:,1].argsort()]
# print(rules)

rulist = {}
b_sel = rules[0][1]
grouped = []
for a, b in rules:
    if b == b_sel:
        grouped.append(a)
    else:
        rulist[b_sel] = list(np.sort(grouped))
        b_sel = b
        grouped = [a]
    rulist[b_sel] = list(np.sort(grouped))
# print(rulist)

count = 0
with open(f'{sys.argv[1]}B.txt', 'r') as f:
    updates = f.readlines()
    for update in updates:
        flag = True
        update_list = [int(el) for el in update.split(',')]

        for i, a in enumerate(update_list):
            if a not in rulist.keys(): continue
            rule = rulist[a]
            for j, b in enumerate(update_list[i+1:]):
                if b in rule:
                    flag = False
                    break

        if flag == False:
            # print(f"Wrong: {update_list}")
            for k in range(10):
                for i, a in enumerate(update_list):
                    if a not in rulist.keys(): continue
                    else:
                        rule = rulist[a]
                        for j, b in enumerate(update_list[i+1:]):
                            if b in rule:
                                update_list = swap(i, i + 1 + j, update_list)
                                # print(f"swap {a, b}")
            # print(f"Corrected: {update_list}")
            count += update_list[int(np.floor(len(update_list)/2))]

print(count)

                