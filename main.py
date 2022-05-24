from setup import *
from cell import *

if __name__ == '__main__':
    visual = False
    verbose = True


    if visual:
        fig = plt.figure(dpi=160)

        for index, transf in enumerate(stateToTrans):
            if transf == 0:
                Node(index).visualize(fig, stateToClass[index])

        plt.savefig("equivs.png")
    
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

