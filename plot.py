from setup import *
from fragments import *
matplotlib.use('WebAgg')


def prepForPrint(str):
    if str == '':
        return 0
    
    return ''.join(x.title() for x in str.split('_'))


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
    ax.view_init(30, -70)

    fs = [
        '',
        'corner_cave_up',
        '',
        '',
        '',
        '',
        'edge_cave_vert',
        'edge_cave_vert',
   ]
    ts = [
	    0, 2, 0, 0, 0, 0, 0, 0
    ]

    for i in range(8):
        if fs[i] != '':
            mesh_dict[fs[i]].draw(ax, quadrant=i, transform=ts[i])

    fs_out = [prepForPrint(filename) for filename in fs]

    print(str(fs_out).replace('\'', '').replace('[', '{').replace(']', '}'), end=',\n')
    print(str(ts).replace('[', '{').replace(']', '}'), end=',\n')

    # plt.savefig("plot.png")

    plt.show()




