from demo import *
import random

def test_max_min():
    arr = []
    for x in range(0, 10):
        a.append(random.randint(10, 99))

    m = max_min(arr)

    for s in arr:
        assert(m >= s)
