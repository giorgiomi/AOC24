import numpy as np

def createDictionary(data):
    dict = {}
    for i in range(len(data)):
        for j in range(len(data[i])):
            antenna = data[i][j]
            if antenna != '.':
                if antenna in dict.keys():
                    dict[antenna].append((i, j))
                else:
                    dict.update({antenna: [(i, j)]})
    return dict

data = np.loadtxt('input.txt', dtype=str)
dict = createDictionary(data)

locations = set()
for key in dict.keys():
    # print(key)
    # print(dict[key])
    for a in dict[key]:
        for b in dict[key]:
            if a != b:
                #print(a, b)
                n1 = [2 * b[0] - a[0], 2 * b[1] - a[1]]
                #print(n1)
                n2 = [- b[0] + 2 * a[0], - b[1] + 2 * a[1]]
                #print(n1, n2)
                locations.add(tuple(n1))
                locations.add(tuple(n2))

locations = [el for el in locations if el[0] >= 0 and el[1] >= 0 and el[0] <= len(data) - 1 and el[1] <= len(data[0]) - 1]

print(len(set(locations)))
