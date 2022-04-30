from setup import *
from cell import *

if __name__ == '__main__':
    stateToClass = [-1 for _ in range(256)]
    stateToTrans = ['' for _ in range(256)]
    classToStates = []

    fig = plt.figure(dpi=160)

    for i in range(256):
        node = Node(i)

        equivs = node.equivalencies()

        idens = ['', 'r', 'rr', 'rrr', 'x', 'xr', 'xrr' 'xrr', 'y', 'yr', 'yrr', 'yrrr']

        # Check if class already exists for this state
        candidateClass = stateToClass[min(equivs)]
        
        # If class does not already exist for this state
        if candidateClass == -1:
            for equiv, iden in zip(equivs, idens):
                if stateToClass[equiv] == -1:
                    stateToClass[equiv] = len(classToStates)
                    stateToTrans[equiv] = iden
            classToStates.append(set(equivs))


            node.visualize(fig, len(classToStates) - 1)
    
    plt.savefig("equivs.png")


    """
    # Print equivalency classes
    print('{', end='')
    print(', '.join([str(state) for state in stateToClass]), end='')
    print('}')
    """
