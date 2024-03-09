#!/usr/bin/python3
"""Defines a list of integer addition function"""


def sum(arg):
    """Function sums up a list or tuple of numbers
    """
    num = 0
    for val in arg:
        num += val
    return num
