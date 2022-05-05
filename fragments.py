from setup import *
from cell import *
from trans import *


dirname = '../../games/BasicStalbergTiles'

obj_filenames = [filename for filename in os.listdir(dirname) if filename.endswith('.obj')]



class Mesh:
    def __init__(self, filename) -> None:
        mesh = om.read_trimesh(filename, vertex_normal=True)
        verts = mesh.points()
        polys = mesh.face_vertex_indices()

        self.verts = verts.copy()
        # self.verts[:, [0, 1]] = self.verts[:, [1, 0]]
        self.verts[:, [0, 1]] *= -1
        self.polys = polys.copy()

    def draw(self, ax, quadrant=0, transform=0):
        verts = (self.verts @ transforms[transform].T) + 2 * moddedPositions[quadrant, :]
        collection = [
            verts[poly, :] for poly in self.polys
        ]
        
        ax.add_collection3d(Poly3DCollection(collection))


mesh_dict = {}
for filename in obj_filenames:
    mesh_dict[filename[:-4]] = Mesh(os.path.join(dirname, filename))
