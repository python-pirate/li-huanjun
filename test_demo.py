from demo import *
import random

def test_max_min():
    a = []

    for i in range(0, 10):
        a.append(random.randint(10, 99))
        
    res = max_min(a)

    for i in a:
        assert(res >= i)
