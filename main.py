#!/usr/bin/python
import sys
from useful_package import hyperbola, polynom_3

if __name__ == "__main__":
    x = sys.argv[1]

    print(x, polynom_3(x), yperbola(x))
