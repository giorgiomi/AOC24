import numpy as np
from copy import deepcopy

def numberDigits(n):
    return int(np.floor(np.log10(float(n)))) + 1

def splitNumber(n):
    n_str = str(n)
    return (int(n_str[:int(len(n_str)/2)]), int(n_str[int(len(n_str)/2):]))

def blink(dict):
    new_dict = deepcopy(dict)
    for key in dict.keys():
        if key == 0:
            if 1 in new_dict: 
                new_dict[1] += dict[0]
            else: 
                new_dict.update({1:dict[0]})
        elif numberDigits(key) % 2 == 0:
            key1, key2 = splitNumber(key)
            # print(key1, key2)
            if key1 in new_dict: 
                new_dict[key1] += dict[key]
            else: 
                new_dict.update({key1:dict[key]})
            if key2 in new_dict: 
                new_dict[key2] += dict[key]
            else: 
                new_dict.update({key2:dict[key]})        
        else:
            if key*2024 in new_dict: 
                new_dict[key*2024] += dict[key]
            else: 
                new_dict.update({key*2024:dict[key]})   
        new_dict[key] -= dict[key]
        if new_dict[key] == 0:
            del new_dict[key]
    # print(new_dict)
    return new_dict

data = np.loadtxt('input.txt', dtype=int)
dict = {el:1 for el in data}
print(dict)

N = 75
for i in range(N):
    # print(i)
    dict = blink(dict)
# print(dict)
print(sum(dict.values()))
