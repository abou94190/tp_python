import unittest
import math


def sqrt(x):
    if x < 0:
        raise ValueError("x doit etre un positif")
    return math.sqrt(x)
