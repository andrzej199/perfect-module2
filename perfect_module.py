#!usr/bin/env python3.7.3

"""this module add two digits and return result

Usage:
    python perfect-module.py <param1> <param2>
    ./perfect_module.py <param1> <param2>
    from perfect_module import add
    import prfect_module
    perfect_module.add(param1, param2)
"""

import sys


def add(a, b):
    """
    Add two digits and return result
    :param a: Digit as integer or float
    :param b: Digit as integer or float
    :return:  A sum of two digit
    """
    return a+ b

if __name__ = '__main__':
    try:
        add(float(sys.argv[1]), float(sys.argv[2]))
    except Exceptions as error:
        print('Ziomeczku złe parametry')
