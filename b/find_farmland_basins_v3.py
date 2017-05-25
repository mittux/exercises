import numpy as np
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

input_matrix = np.array(input_matrix)
expected_result = np.array(expected_result)
print(input_matrix)

result = np.empty_like(input_matrix)

basins = np.chararray(input_matrix.shape)
basins[:] = 'B'
left_dir = np.chararray(input_matrix.shape)
left_dir[:] = 'l'
right_dir = np.chararray(input_matrix.shape)
right_dir[:] = 'r'
down_dir = np.chararray(input_matrix.shape)
down_dir[:] = 'd'
up_dir = np.chararray(input_matrix.shape)
up_dir[:] = 'u'

down = np.roll(input_matrix, -1, axis=0)
down_cmp = down - input_matrix
down_cmp[5] *= 0

up = np.roll(input_matrix, 1, axis=0)
up_cmp = up - input_matrix
up_cmp[0] *= 0

left = np.roll(input_matrix, 1, axis=1)
left_cmp = left - input_matrix
left_cmp[:, 0] *= 0

right = np.roll(input_matrix, -1, axis=1)
right_cmp = right - input_matrix
right_cmp[:, 4] *= 0

left_right = np.fmin(left_cmp, right_cmp)
left_right_dir = np.where(left_cmp < right_cmp, left_dir, right_dir)
up_down = np.fmin(up_cmp, down_cmp)
up_down_dir = np.where(up_cmp < down_cmp, up_dir, down_dir)
minimum = np.fmin(left_right, up_down)
direction = np.where(left_right < up_down, left_right_dir, up_down_dir)

#print(minimum) 

final_direction = np.where(minimum == 0, basins, direction)

print(final_direction)

result = input_matrix + minimum
# print(result)

def find_next_cell(i, j, dir):
    dir = dir.decode('utf-8')
    if dir == 'u':
        return i-1, j
    if dir == 'd':
        return i+1, j
    if dir == 'r':
        return i, j+1
    if dir == 'l':
        return i, j-1
    return i, j

# make an initial dictionary
d = {}
for i in range(6):
    for j in range(5):
            cell = '%d_%d' % (i,j)
            next_cell = '%d_%d' % find_next_cell(i, j, final_direction[i,j])
            d[cell] = next_cell, final_direction[i,j] == b'B'
#pprint(d)

final_d = {}

# now compute till each entry reaches a basin
keep_going = True
while keep_going:
    keep_going = False
    for k,v in d.items():
        n, basin = v
        if basin:
            final_d[k] = n
        else:
            d[k] = d[n]
            keep_going = True

#pprint(final_d)

for k,v in final_d.items():
    i,j = map(int, k.split('_'))
    x,y = map(int, v.split('_'))
    result[i, j] = input_matrix[x, y]

print(result)
#print(expected_result)

if np.array_equal(expected_result, result):
	print('Pass!')
else:
	print('Fail!')
