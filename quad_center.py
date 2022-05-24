from setup import *


def get_line_between_points(p1, p2):
    a = p2[1] - p1[1]
    b = p1[0] - p2[0]
    c = p1[0] * p2[1] - p1[1] * p2[0]
    return (a, b, c)


def get_intersection_between_lines(l1, l2):
    det_inv = 1 / (l1[0] * l2[1] - l2[0] * l1[1])
    x = l1[2] * l2[1] - l2[2] * l1[1]
    y = l2[2] * l1[0] - l1[2] * l2[0]
    return (x * det_inv, y * det_inv)


if __name__ == '__main__':
    p = np.random.rand(4, 2)

    """
    p = np.array([
        [10, 1],
        [-1, 10],
        [-1, -10],
        [1, -1],
    ])
    """

    l1 = get_line_between_points(p[0,:], p[2,:])
    l2 = get_line_between_points(p[1,:], p[3,:])
    center = get_intersection_between_lines(l1, l2)

    p = np.vstack((p, center))

    plt.figure()

    l1_points = np.array([0, 2])
    l2_points = np.array([1, 3])

    plt.plot(p[:,0][l1_points], p[:,1][l1_points], marker='o')
    plt.plot(p[:,0][l2_points], p[:,1][l2_points], marker='o')
    plt.plot(p[:,0][4], p[:,1][4], marker='o')


    plt.savefig('quad_center.png')
