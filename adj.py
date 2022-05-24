from setup import *
from cell import *


# this determines whether two node states
# can be placed next to each other 
def are_horizontal_connectible(back_node: Node, front_node: Node) -> bool:
    return back_node.state & 0b1111 == (front_node.state & 0b11110000) >> 4



if __name__ == '__main__':

    num_adjs = 0
    for i in range(256):
        for j in range(256):
            if are_horizontal_connectible(Node(i), Node(j)):
                num_adjs += 1

    print(num_adjs)
