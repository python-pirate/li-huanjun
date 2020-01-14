from demo import *
import random


def test_max_min():
    for x in range(10000):
        arr = []
        for x in range(10):
            arr.append(random.randint(10, 99))

        m = max_min(arr)

        for s in arr:
            assert(m >= s)
