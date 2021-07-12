import numpy


def arrays(arr):
    numpy.flipud
    return numpy.array(arr[::-1], float)


arr = "1 2 3 4 -8 -10".strip().split(' ')
result = arrays(arr)
print(result)
