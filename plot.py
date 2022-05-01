from setup import *
from fragments import *


if __name__ == '__main__':
    fig = plt.figure()
    ax = Axes3D(fig, auto_add_to_figure=False)
    fig.add_axes(ax)

    ax.set_zlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_xlim(-2, 2)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    DentedVexUp(quadrant=0, transform=0).draw(ax)

    plt.show()




