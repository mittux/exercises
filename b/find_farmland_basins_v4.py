from pprint import pprint

input_matrix = [ [1, 0, 2, 3, 9],
                 [3, 5, 6, 7, 10],
                 [11, 8 ,20, 5, 8],
                 [17, 16, 15, 4, 14],
                 [20, 25 ,14 ,3, 21], 
                 [19, 18, 13, 2, 12] ]

expected_result = [ [0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0],
                    [0, 0, 2, 2, 2],
                    [0, 0, 2, 2, 2],
                    [0, 2, 2, 2, 2],
                    [2, 2, 2, 2, 2] ]

pprint(input_matrix)
pprint(expected_result)

m, n = len(input_matrix), len(input_matrix[0])

def valid_x(x):
    if x < 0 or x > m-1:
        raise Exception("Invalid x")
    return x

def valid_y(y):
    if y < 0 or y > n-1:
        raise Exception("Invalid y")
    return y

def find_smallest_neighbour(x,y):
    neigbours = []
    try:
        centre = valid_x(x), valid_y(y)
        vcentre = input_matrix[x][y]
        neigbours.append((centre, vcentre))
    except:
        pass
    try:
        left = valid_x(x-1),valid_y(y)      
        vleft = input_matrix[x-1][y]
        neigbours.append((left, vleft)) 
    except:
        pass
    try:
        right = valid_x(x+1),valid_y(y)
        vright = input_matrix[x+1][y]
        neigbours.append((right, vright))
    except:
        pass
    try:
        top = valid_x(x),valid_y(y-1)
        vtop = input_matrix[x][y-1]
        neigbours.append((top, vtop))
    except:
        pass
    try:
        bottom = valid_x(x),valid_y(y+1)
        vbottom = input_matrix[x][y+1]
        neigbours.append((bottom, vbottom))
    except:
        pass
    neigbours.sort(key=lambda e: e[1])
    return neigbours[0]

smallest_neigbours = [ [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0] ]


for i in range(m):
    for j in range(n):
        smallest_neigbours[i][j] = find_smallest_neighbour(i,j)

pprint(smallest_neigbours)

basins = [ [None, None, None, None, None],
           [None, None, None, None, None],
           [None, None, None, None, None],
           [None, None, None, None, None],
           [None, None, None, None, None],
           [None, None, None, None, None] ]

def find_basin(x,y):
    basin = basins[x][y]
    if basin is not None:
        return basin
    smallest_neigbour = smallest_neigbours[x][y]
    if smallest_neigbour[0][0] == x and smallest_neigbour[0][1] == y:
        return smallest_neigbour[1]
    else:
        return find_basin(*smallest_neigbour[0])

for i in range(m):
    for j in range(n):
        basins[i][j] = find_basin(i,j)

pprint(basins)

if expected_result == basins:
    print('Pass!')
else:
    print('Fail!')