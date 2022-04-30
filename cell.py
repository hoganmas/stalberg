from setup import *


def stateFromSet(nums: set) -> int:
    state = 0
    for i in range(8):
        if i in nums:
            state ^= 1 << i
    return state


def setFromState(state: int) -> set:
    nums = set()
    for i in range(8):
        if (1 << i) & state != 0:
            nums.add(i)
    return nums


positions = np.array([
    [1, 1, 1],  # front top right
    [1, 1, -1], # front bottom right
    [1, -1, 1], # front top left
    [1, -1, -1],# front bottom left
    [-1, 1, 1], # back top right
    [-1, 1, -1],
    [-1, -1, 1],
    [-1, -1, -1],
]) * 0.5


moddedPositions = np.array([
    [1, 1, 1],  # front top right
    [1, 1, -1], # front bottom right
    [-1, 1, 1], # front top left
    [-1, 1, -1],# front bottom left
    [1, -1, 1], # back top right
    [1, -1, -1],
    [-1, -1, 1],
    [-1, -1, -1],
]) * 0.5

# INVARIANT TRANSFORMATIONS
rotator = np.array([2, 3, 6, 7, 0, 1, 4, 5,])
reflectorX = np.array([2, 3, 0, 1, 6, 7, 4, 5,])
reflectorY = np.array([4, 5, 6, 7, 0, 1, 2, 3,])

def rotateSet(nums: set) -> set:
    return set([rotator[num] for num in nums])

def reflxSet(nums: set) -> set:
    return set([reflectorX[num] for num in nums])

def reflySet(nums: set) -> set:
    return set([reflectorY[num] for num in nums])


class Node:
    def __init__(self) -> None:
        self.state = 0
        

    def __init__(self, state) -> None:
        if isinstance(state, set):
            self.state = stateFromSet(state)
        elif isinstance(state, int):
            self.state = state
        else:
            state = int(state)
    

    def equivalencies(self):
        nums = setFromState(self.state)
        equivs = []

        reflx = reflxSet(nums)
        refly = reflySet(nums)

        for base, prefix in zip([nums, reflx, refly], ['', 'x', 'y']):
            equivs.append(stateFromSet(base))
            rotated = base
            for i in range(3):
                rotated = rotateSet(rotated)
                equivs.append(stateFromSet(rotated))

        # NOTE: Can also create a way to backtrack which
        # transformations result in each equivalency.
        # This would probably be really important 

        return equivs


    def visualize(self, fig, equiv):
        nums = setFromState(self.state)

        ax = fig.add_subplot(7, 8, equiv + 1, projection='3d')
        xs = []
        ys = []
        zs = []

        vs = moddedPositions[list(nums)]

        print(equiv, vs)

        ax.scatter(vs[:,0], vs[:,1], vs[:,2])
        # ax.set_xlabel('X-axis')
        # ax.set_ylabel('Y-axis')
        # ax.set_ylabel('Z-axis')
        ax.set_zticklabels([])
        ax.set_yticklabels([])
        ax.set_xticklabels([])

        ax.set_zlim(-0.5, 0.5)
        ax.set_ylim(-0.5, 0.5)
        ax.set_xlim(-0.5, 0.5)

        if equiv % 8 == 0:
            ax.set_title(str(equiv))
        
        return ax

        for i in range(8):
            if i in nums:
                xs.append(moddedPositions[i,])
    
        for i in range(8):
            if i in nums:
                vpython.box(
                    pos=vpython.vector(*moddedPositions[i]),
                )
            else:
                vpython.sphere(
                    pos=vpython.vector(*moddedPositions[i]),
                    radius=0.01
                )


