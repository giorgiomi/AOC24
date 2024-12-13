import numpy as np

def partialPerimeter(i, j, data):
    plant = data[i][j]
    count = 0
    if (i > 0 and data[i-1][j] != plant) or i == 0:
        count += 1
    if (j < len(data[i]) - 1 and data[i][j+1] != plant) or j == len(data[i]) - 1:
        count += 1
    if (i < len(data) - 1 and data[i+1][j] != plant) or i == len(data) - 1:
        count += 1
    if (j > 0 and data[i][j-1] != plant) or j == 0:
        count += 1
    return count

def regionCost(data, region):
    per = 0
    area = 0
    for plantPos in region:
        # print(plantPos, end=' ')
        partial_per = partialPerimeter(plantPos[0], plantPos[1], data)
        # print(partial_per)
        per += partial_per
        area += 1
    return area, per

def move(i, j, data, region):
    plant = data[i][j]
    region.add((i, j))
    
    if i > 0 and plant == data[i-1][j] and (i-1, j) not in region:
        region.add((i-1, j))
        region = move(i-1, j, data, region) #N
    if j < len(data[i]) - 1 and plant == data[i][j+1] and (i, j+1) not in region:
        region.add((i, j+1))
        region = move(i, j+1, data, region) #E
    if i < len(data) - 1 and plant == data[i+1][j] and (i+1, j) not in region:
        region.add((i+1, j))
        region = move(i+1, j, data, region) #S
    if j > 0 and plant == data[i][j-1] and (i, j-1) not in region:
        region.add((i, j-1))
        region = move(i, j-1, data, region) #W
    return region


data = np.loadtxt('input.txt', dtype=str)
# print(partialPerimeter(1, 8, data))

visited = set()
cost = 0
for i in range(len(data)):
    for j in range(len(data[i])):
        if (i, j) in visited:
            continue
        else:
            region = set()
            region = move(i, j, data, region)
            visited.update(region)

            area, per = regionCost(data, region)
            cost += per*area
            # print(area, per)
print(cost)
# print(visited)
