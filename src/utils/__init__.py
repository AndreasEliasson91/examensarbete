import os
import sys


def devnull(x) -> None:
    """
    Function to print to devnull,
    to prevent results from potentially being removed in optimization
    """
    stdout = sys.stdout

    with open(os.devnull, 'w') as f:
        sys.stdout = f

        try:
            print(len(x))
        except TypeError:
            print(x)

    sys.stdout = stdout