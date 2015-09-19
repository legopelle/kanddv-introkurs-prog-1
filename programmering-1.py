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
