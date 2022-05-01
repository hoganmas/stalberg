from setup import *

transforms = [
    np.identity(3, dtype=int),
    np.array([
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ]),
    np.array([
        [-1, 0, 0],
        [0, -1, 0],
        [0, 0, 1],
    ]),
    np.array([
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1],
    ]),
]

reflX = np.array([
    [-1, 0, 0],
    [0, 1, 0],
    [0, 0, 1],
])

reflections = [reflX @ transform for transform in transforms]
transforms += reflections


def areEqual(A, B):
    return np.sum((A - B) ** 2) == 0


def printInverses():
    for this in transforms:
        for index, other in enumerate(transforms):            
            if areEqual(np.linalg.inv(this), other):
                print(index)


def printQuotients():
    quotients = -1 * np.ones((8, 8), dtype=int)

    for i, this in enumerate(transforms):
        for j, other in enumerate(transforms):
            for k, transform in enumerate(transforms):
                if areEqual(other @ np.linalg.inv(this), transform):
                    quotients[i, j] = k
                    # print("When viewed from {}, {} looks like {}".format(i, j, k))

    print('{', end='')
    for i in range(8):
        print('\n\t{', end='')
        for j in range(8):
            if i == 7 and j == 7:
                print(quotients[i, j], end='}\n}\n')
            elif j == 7:
                print(quotients[i, j], end='},')
            else:
                print(quotients[i, j], end=', ')


def printProducts():
    products = -1 * np.ones((8, 8), dtype=int)

    for i, this in enumerate(transforms):
        for j, other in enumerate(transforms):
            for k, transform in enumerate(transforms):
                if areEqual(other @ this, transform):
                    products[i, j] = k
                    print("Applying {} then {} looks like {}.".format(i, j, k))

    print('{', end='')
    for i in range(8):
        print('\n\t{', end='')
        for j in range(8):
            if i == 7 and j == 7:
                print(products[i, j], end='}\n}\n')
            elif j == 7:
                print(products[i, j], end='},')
            else:
                print(products[i, j], end=', ')




if __name__ == '__main__':
    printProducts()
