from setup import *
from cell import *

if __name__ == '__main__':
    stateToClass = [-1 for _ in range(256)]
    stateToTrans = ['o' for _ in range(256)]
    classToStates = []

    visual = False
    verbose = True

    if visual:
        fig = plt.figure(dpi=160)

    for i in range(256):
        node = Node(i)

        equivs = node.equivalencies()

        idens = ['', '1', '2', '3', 'x', 'x1', 'x2', 'x3', 'y', 'y1', 'y2', 'y3']
        idens = range(12)

        # Check if class already exists for this state
        candidateClass = stateToClass[min(equivs)]
        
        # If class does not already exist for this state
        if candidateClass == -1:
            for equiv, iden in zip(equivs, idens):
                if stateToClass[equiv] == -1 or iden < stateToTrans[equiv]:
                    stateToClass[equiv] = len(classToStates)
                    stateToTrans[equiv] = iden
            classToStates.append(set(equivs))

            if visual:
                node.visualize(fig, len(classToStates) - 1)
    
    if visual:
        plt.savefig("equivs.png")
    
    print(min(stateToTrans), max(stateToTrans))


    if verbose:
        perLine = 16

        # Print equivalency classes
        print("CLASS TABLE")
        print('{', end='')

        for index, state in enumerate(stateToClass):
            if index == len(stateToClass) - 1:
                print(str(state))
            else:
                if index % perLine == 0:
                    print('\n\t', end='')
                print('{}, '.format(state), end='')
        print('}')

        print("\nTRANSFORMATION TABLE")
        
        # Print equivalency classes
        print("CLASS TABLE")
        print('{', end='')

        for index, trans in enumerate(stateToTrans):
            if index == len(stateToTrans) - 1:
                print(str(trans))
            else:
                if index % perLine == 0:
                    print('\n\t', end='')
                print('{}, '.format(trans), end='')
        print('}')

