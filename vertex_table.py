from trans import *
from cell import *


def print_vertex_table():

    # for each transformation
    table = np.reshape(np.arange(8, dtype=int), (1, -1))

    for _ in range(3):
        new_row = np.reshape([rotator[num] for num in table[-1,:]], (1, -1))
        table = np.append(table, new_row, axis=0)
    
    new_row = np.reshape([reflectorX[num] for num in table[0,:]], (1, -1))
    table = np.append(table, new_row, axis=0)

    for _ in range(3):
        new_row = np.reshape([rotator[num] for num in table[-1,:]], (1, -1))
        table = np.append(table, new_row, axis=0)
    
    print('{', end='')
    for i in range(8):
        print('\n\t{', end='')
        for j in range(8):
            if i == 7 and j == 7:
                print(table[i, j], end='}\n}\n')
            elif j == 7:
                print(table[i, j], end='},')
            else:
                print(table[i, j], end=', ')



if __name__ == '__main__':
    print_vertex_table()

