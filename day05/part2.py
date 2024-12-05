import numpy as np
from numpy._core.defchararray import count

rules = np.loadtxt('inputA.txt', delimiter='|', dtype=int)
rules = rules[rules[:,0].argsort()]
#print(rules)

# REDONE the not PSYCHOPATH way
rulist = {}
a_prev = rules[0][0]
grouped = []
for a, b in rules:
    if a == a_prev:
        grouped.append(b)
    else:
        rulist[a_prev] = list(np.sort(grouped))
        a_prev = a
        grouped = [b]

#for k in rulist.keys():
#    print(k, rulist[k])
#exit()


def check_rules(update_list, rulist):

    for i, a in enumerate(update_list):
        if a not in rulist.keys():
            continue

        rule = rulist[a]
        for j, b in enumerate(update_list[:i]):
            if b in rule:
                return False

    return True


def correct_list(update_list, rulist):
    # a b c d
    # if rule c | a 
    # b c a d
    # I biliv

    for i, el in enumerate(update_list):
        if el not in rulist.keys():
            continue

        for j, el2 in enumerate(update_list[:i]):
            
            if el2 in rulist[el]:
                #print(el, rulist[el])
                #print(update_list)
                update_list.pop(j)
                update_list.insert(i, el2)
                #print(update_list)
                break

    return update_list
            

count = 0
count2 = 0
with open('inputB.txt', 'r') as f:
    updates = f.readlines()
    for update in updates:

        update_list = [int(el) for el in update.split(',')]

        follows_rules = check_rules(update_list, rulist)

        if follows_rules:
            count += update_list[int(np.floor(len(update_list)/2))]
        else:
            follows_rules = False
            kk = 0 
            while follows_rules == False:
                kk += 1
                corr_list = correct_list(update_list, rulist)
                follows_rules = check_rules(update_list, rulist)
            print(kk)
            
            #print('-'*40)
            count2 += corr_list[int(np.floor(len(corr_list)/2))]


print(count)
print(count2)
                
