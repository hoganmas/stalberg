from setup import *
from cell import *
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from trans import *


class Fragment:
    def draw(self, ax):        
        collection = [
            self.verts[poly, :] for poly in self.polys
        ]
        
        ax.add_collection3d(Poly3DCollection(collection))





class DentedVexUp(Fragment):
    def __init__(self, quadrant=0, transform=0) -> None:
        super().__init__()

        self.verts = np.array([
            [1, 1, 0],
            [1, -1, 0],
            [0, -1, 0],
            [-1, -1, 1],
            [-1, 0, 0],
            [-1, 1, 0]
        ], dtype=float)

        self.verts = self.verts @ transforms[transform].T

        self.polys = [
            [0, 1, 2, 4, 5],
            [2, 3, 4]
        ]

        self.verts += 2 * positions[quadrant, :]
