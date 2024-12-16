import numpy as np

rules = np.loadtxt('inputA.txt', delimiter='|', dtype=int)
rules = rules[rules[:,1].argsort()]
#print(rules)

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

# print(rulist[18])
# print([len(rulist[k][1]) for k in range(len(rulist))])
# print(len(rulist))
# exit()

count = 0
with open('inputB.txt', 'r') as f:
    updates = f.readlines()
    for update in updates:
        flag = True
        update_list = [int(el) for el in update.split(',')]
        #print(update_list)
        for i,a in enumerate(update_list):
            if flag == False: continue
            if a not in rulist.keys(): continue
            rule = rulist[a]
            for j,b in enumerate(update_list[i+1:]):
                if b in rule:
                    flag = False
                    break
        if flag == True:
            count += update_list[int(np.floor(len(update_list)/2))]
print(count)

                