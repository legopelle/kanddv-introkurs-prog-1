#!/bin/env python2


def double(x):
    """Doubles numbers

    :x: Number to be doubled
    :returns: Double x

    """
    return 2*x


def quadruple(x):
    """Quadruples numbers

    :x: Number to be quadrupled
    :returns: Quadrupled x

    """
    return double(double(x))


def max2(x, y):
    """Returns the largest of two objects

    :x: First object
    :y: Second object
    :returns: Largest object

    """

    # Mean of the numbers
    mean = 0.5*(x + y)

    # Absolute half difference between the numbers
    halfdiff = 0.5*abs(x-y)
    return mean + halfdiff


def max3(x, y, z):
    """Returns the largest of three numbers

    :x: First number
    :y: Second number
    :z: Third number
    :returns: Largest number

    """

    return max2(max2(x, y), z)


def magic_sum(x, y, z):
    """Returns the sum of the quadrupled largest and second largest numbers

    :x: First number
    :y: Second number
    :z: Third number
    :returns: The sum of the quadrupled largest and second largest numbers

    """

    largest = max3(x, y, z)
    first_term = quadruple(largest)

    if largest == x:
        middle = max2(y, z)
    elif largest == y:
        middle = max2(x, z)
    elif largest == z:
        middle = max2(x, y)
    else:
        raise ValueError('Comparing largest number with input numbers failed')

    second_term = quadruple(middle)

    return first_term + second_term


assert double(2) == 2*2

assert max2(2, 3) == 3
assert max2(0.0001, -0.0002) > 0
assert max2(-1, -5) == -1

assert magic_sum(1, 2, 3) == 2*4 + 3*4
assert magic_sum(-5, -2, -1) == -4*1 + -4*2
