import numpy as np

def corners(i, j, data):
    i_max = len(data) - 1
    j_max = len(data[i]) - 1
    plant = data[i][j]
    plant_corners = set()
    if i > 0: north = data[i-1][j]
    if j < j_max: east = data[i][j+1]
    if i < i_max: south = data[i+1][j]
    if j > 0: west = data[i][j-1]

    # NW corner
    if i > 0 and j > 0:
        if north == plant and west == plant:
            if data[i-1][j-1] != plant:
                plant_corners.add((i, j, 'NW'))
        elif north != plant and west != plant:
            plant_corners.add((i, j, 'NW'))
    elif i == 0 and j > 0:
        if west != plant:
            plant_corners.add((i, j, 'NW'))
    elif j == 0 and i > 0:
        if north != plant:
            plant_corners.add((i, j, 'NW'))
    else:
        plant_corners.add((i, j, 'NW'))
    
    # NE corner
    if i > 0 and j < j_max:
        if north == plant and east == plant:
            if data[i-1][j+1] != plant:
                plant_corners.add((i, j+1, 'NE'))
        elif north != plant and east != plant:
            plant_corners.add((i, j+1, 'NE'))
    elif i == 0 and j < j_max:
        if east != plant:
            plant_corners.add((i, j+1, 'NE'))
    elif j == j_max and i > 0:
        if north != plant:
            plant_corners.add((i, j+1, 'NE'))
    else:
        plant_corners.add((i, j+1, 'NE'))
    
    # SE corner
    if i < i_max and j < j_max:
        if south == plant and east == plant:
            if data[i+1][j+1] != plant:
                plant_corners.add((i+1, j+1, 'SE'))
        elif south != plant and east != plant:
            plant_corners.add((i+1, j+1, 'SE'))
    elif i == i_max and j < j_max:
        if east != plant:
            plant_corners.add((i+1, j+1, 'SE'))
    elif j == j_max and i < i_max:
        if south != plant:
            plant_corners.add((i+1, j+1, 'SE'))
    else:
        plant_corners.add((i+1, j+1, 'SE'))
    
    # SW corner
    if i < i_max and j > 0:
        if south == plant and west == plant:
            if data[i+1][j-1] != plant:
                plant_corners.add((i+1, j, 'SW'))
        elif south != plant and west != plant:
            plant_corners.add((i+1, j, 'SW'))
    elif i == i_max and j > 0:
        if west != plant:
            plant_corners.add((i+1, j, 'SW'))
    elif j == 0 and i < i_max:
        if south != plant:
            plant_corners.add((i+1, j, 'SW'))
    else:
        plant_corners.add((i+1, j, 'SW'))

    return plant_corners


def regionCost(data, region):
    n_sides = 0
    area = 0
    region_corners = set()
    for plantPos in region:
        # calculate number of corners instead of perimeter
        plant_corners = corners(plantPos[0], plantPos[1], data)
        region_corners.update(plant_corners)
        area += 1
    # print(region_corners)
    n_sides = len(region_corners)
    return area, n_sides

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

            area, n_sides = regionCost(data, region)
            cost += n_sides*area
            print(area, n_sides)
print(cost)
# print(visited)
